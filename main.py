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
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()
        self.gamestatus = True

    def load_data(self):
        # load data
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'default size img')
        map_folder = path.join(game_folder, 'maps')
        # self.map = Map(path.join(game_folder, 'map.txt'))
        self.map = TiledMap(path.join(map_folder, 'testmap1.tmx'))
        self.map_img = self.map.make_map()
        self.map_rect = self.map_img.get_rect()
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
        self.bullet_img = pg.image.load(path.join(img_folder, BULLET_IMG)).convert_alpha()
        self.mob_img = pg.image.load(path.join(img_folder, MOB_IMG)).convert_alpha()
        self.wall_img = pg.image.load(path.join(img_folder, WALL_IMG)).convert_alpha()
        self.wall_img = pg.transform.scale(self.wall_img, (TILESIZE, TILESIZE))

    def new(self):
        # set all variables to create a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.bullets = pg.sprite.Group()

        # for row, tiles in enumerate(self.map.data):
        #    for col, tile in enumerate(tiles):
        #       if tile == '1':
        #           Wall(self, col, row)
        #       if tile == 'M':
        #           Mob(self, col, row)
        #       # Spawnpoint Player
        #       if tile == 'P':
        #           self.player = Player(self, col, row)
        self.player = Player(self, 5, 5)
        self.camera = Camera(self.map.width, self.map.height)

        self.run()

    def run(self):
        # Game loop
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # Game loop - update
        self.all_sprites.update()
        self.camera.update(self.player)
        #mobs hit player
        hits = pg.sprite.spritecollide(self.player, self.mobs, False, collide_hit_rect)
        for hit in hits:
            self.player.health -= MOB_DAMAGE
            hit.vel = vec(0, 0)
            if self.player.health <= 0:
                self.playing = False
        if hits:
            self.player.pos += vec(MOB_KNOCKBACK, 0).rotate(-hits[0].rot)
        # bullet hit mobs
        hits = pg.sprite.groupcollide(self.mobs, self.bullets, False, True)
        for hit in hits:
            hit.health -= BULLET_DAMAGE
            hit.vel = vec(0, 0)

    # Gitternetz
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        # Game loop - draw
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        # self.screen.fill(BGCOLOR)
        self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
        # self.draw_grid()
        for sprite in self.all_sprites:
            if isinstance(sprite, Mob):
                sprite.draw_health()
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        # pg.draw.rect(self.screen, WHITE, self.player.hit_rect, 2)
        # after drawing everything, flip the window
        # HUD functions
        draw_player_health(self.screen, 10, 10, self.player.health / PLAYER_HEALTH)
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

    def show_start_screen(self):
        # Start screen
        pass

    def show_go_screen(self):
         # Game Over screen
        pass

g = Game()
g.show_start_screen()
while g.gamestatus:
    g.new()
    g.run()
    g.show_go_screen()

pg.quit()