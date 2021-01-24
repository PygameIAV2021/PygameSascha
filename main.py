# Project Pygame in SKP

import pygame
import random
import sys
from os import path
from settings import *
from sprite import *
from tilemap import *

class Game:
    def __init__(self):
        # Initialize Game Window, etc
        pg.mixer.pre_init(44100, -16, 1, 2048)
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()
        self.gamestatus = True

    def draw_text(self, text, font_name, size, color, x, y, align="center"):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == 'center':
            text_rect.center = (x, y)
        if align == 'ne':
            text_rect.topright = (x, y)
        self.screen.blit(text_surface, text_rect)

    def load_data(self):
        # load data
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        music_folder = path.join(game_folder, 'music')
        self.map_folder = path.join(game_folder, 'maps')
        self.title_font = pg.font.match_font('comicsansms')
        self.dim_screen = pg.Surface(self.screen.get_size()).convert_alpha()
        self.dim_screen.fill((0, 0, 0, 190))
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
        self.bullet_images = {}
        self.bullet_images['lg'] = pg.image.load(path.join(img_folder, BULLET_IMG)).convert_alpha()
        self.bullet_images['sm'] = pg.transform.scale(self.bullet_images['lg'], (30, 30))
        self.mob_img = pg.image.load(path.join(img_folder, MOB_IMG)).convert_alpha()
        self.wall_img = pg.image.load(path.join(img_folder, WALL_IMG)).convert_alpha()
        self.wall_img = pg.transform.scale(self.wall_img, (TILESIZE, TILESIZE))
        self.splat = pg.image.load(path.join(img_folder, SPLAT_IMG)).convert_alpha()
        self.splat = pg.transform.scale(self.splat, (64, 64))
        self.explo = []
        for img in EXPLOSION:
            self.explo.append(pg.image.load(path.join(img_folder, img)).convert_alpha())
        self.item_images = {}
        for item in ITEM_IMAGES:
            self.item_images[item] = pg.image.load(path.join(img_folder, ITEM_IMAGES[item])).convert_alpha()
        # lighting effect
        self.fog = pg.Surface((WIDTH, HEIGHT))
        self.fog.fill(NIGHT_COLOR)
        self.light_mask = pg.image.load(path.join(img_folder, LIGHT_MASK)).convert_alpha()
        self.light_mask = pg.transform.scale(self.light_mask, LIGHT_RADIUS)
        self.light_rect = self.light_mask.get_rect()

        # Sound loading
        pg.mixer.music.load(path.join(music_folder, BG_MUSIC))
        self.effects_sounds = {}
        for type in EFFECT_SOUNDS:
            self.effects_sounds[type] = pg.mixer.Sound(path.join(music_folder, EFFECT_SOUNDS[type]))
        self.weapon_sounds = {}
        for weapon in WEAPON_SOUNDS:
            self.weapon_sounds[weapon] = []
            for snd in WEAPON_SOUNDS[weapon]:
                snd_gun = pg.mixer.Sound(path.join(music_folder, snd))
                snd_gun.set_volume(0.3)
                self.weapon_sounds[weapon].append(snd_gun)
        self.enemy_sounds = []
        for snd in ENEMY_SOUNDS:
            snd_enemy = pg.mixer.Sound(path.join(music_folder, snd))
            snd_enemy.set_volume(0.3)
            self.enemy_sounds.append(snd_enemy)
        self.player_hit_sounds = []
        for snd in PLAYER_HIT_SOUNDS:
            snd_playerhit = pg.mixer.Sound(path.join(music_folder, snd))
            snd_playerhit.set_volume(0.3)
            self.player_hit_sounds.append(snd_playerhit)
        self.enemy_hit_sounds = []
        for snd in ENEMY_HIT_SOUNDS:
            snd_enemyhit = pg.mixer.Sound(path.join(music_folder, snd))
            snd_enemyhit.set_volume(0.3)
            self.enemy_hit_sounds.append(snd_enemyhit)

    def new(self):
        # set all variables to create a new game
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.walls = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.items = pg.sprite.Group()
        self.map = TiledMap(path.join(self.map_folder, 'map.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()

        for tile_object in self.map.tmxdata.objects:
            obj_center = vec(tile_object.x + tile_object.width / 2, tile_object.y + tile_object.height / 2)
            if tile_object.name == 'player':
                self.player = Player(self, obj_center.x, obj_center.y)
            if tile_object.name == 'enemy':
                Mob(self, obj_center.x, obj_center.y)
            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
            if tile_object.name in ['health', 'shotgun', 'minigun']:
                Item(self, obj_center, tile_object.name)

        self.camera = Camera(self.map.width, self.map.height)
        self.draw_debug = False
        self.paused = False
        self.night = False
        self.effects_sounds['level_start'].play()

        self.run()

    def run(self):
        # Game loop
        self.playing = True
        pg.mixer.music.play(loops=-1)
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            if not self.paused:
                self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # Game loop - update
        self.all_sprites.update()
        self.camera.update(self.player)
        # game over ?
        if len(self.mobs) == 0:
            self.playing = False
        # player hits items
        hits = pg.sprite.spritecollide(self.player, self.items, False)
        for hit in hits:
            if hit.type == 'health' and self.player.health < PLAYER_HEALTH:
                hit.kill()
                self.effects_sounds['health_up'].play()
                self.player.add_health(HEALTH_PACK_AMOUNT)
            if hit.type == 'shotgun':
                hit.kill()
                self.effects_sounds['health_up'].play()
                self.player.weapon = 'shotgun'
            if hit.type == 'minigun':
                hit.kill()
                self.effects_sounds['health_up'].play()
                self.player.weapon = 'minigun'
        # mobs hit player
        hits = pg.sprite.spritecollide(self.player, self.mobs, False, collide_hit_rect)
        for hit in hits:
            if random() < 0.7:
                choice(self.player_hit_sounds).play()
            self.player.health -= MOB_DAMAGE
            hit.vel = vec(0, 0)
            if self.player.health <= 0:
                self.playing = False
        if hits:
            self.player.hit()
            self.player.pos += vec(MOB_KNOCKBACK, 0).rotate(-hits[0].rot)
        # bullet hit mobs
        hits = pg.sprite.groupcollide(self.mobs, self.bullets, False, True)
        for mob in hits:
            for bullet in hits[mob]:
                mob.health -= bullet.damage
            mob.vel = vec(0, 0)

    # Gitternetz
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def render_fog(self):
        # draw the light mask onto image
        self.fog.fill(NIGHT_COLOR)
        self.light_rect.center = self.camera.apply(self.player).center
        self.fog.blit(self.light_mask, self.light_rect)
        self.screen.blit(self.fog, (0, 0), special_flags=pg.BLEND_MULT)

    def draw(self):
        # Game loop - draw
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        # self.draw_grid()
        for sprite in self.all_sprites:
            if isinstance(sprite, Mob):
                sprite.draw_health()
            self.screen.blit(sprite.image, self.camera.apply(sprite))
            if self.draw_debug:
                pg.draw.rect(self.screen, BLACK, self.camera.apply_rect(sprite.hit_rect), 1)

        if self.night:
            self.render_fog()
        # HUD functions
        draw_player_health(self.screen, 10, 10, self.player.health / PLAYER_HEALTH)
        self.draw_text('Enemys: {}'.format(len(self.mobs)), self.title_font, 30, WHITE, WIDTH - 10, 10, align="ne")
        if self.paused:
            self.screen.blit(self.dim_screen, (0, 0))
            self.draw_text("Paused", self.title_font, 105, YELLOW, WIDTH / 2, HEIGHT / 2, align="center")
        pg.display.flip()

    def events(self):
        # Game loop - events
        # Inputs überprüfen
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.gamestatus = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_p:
                    self.paused = not self.paused
                if event.key == pg.K_n:
                    self.night = not self.night

    def show_start_screen(self):
        # Start screen
        pass

    def show_go_screen(self):
         # Game Over screen
        self.screen.fill(BLACK)
        self.draw_text("GAME OVER", self.title_font, 100, RED, WIDTH / 2, HEIGHT / 2, align="center")
        self.draw_text("Press a key to start", self.title_font, 75, WHITE, WIDTH / 2, HEIGHT * 3 / 4, align="center")
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        pg.event.wait()
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.quit()
                if event.type == pg.KEYUP:
                    waiting = False

g = Game()
g.show_start_screen()
while g.gamestatus:
    g.new()
    g.run()
    g.show_go_screen()

pg.quit()