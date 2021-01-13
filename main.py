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
        pg.key.set_repeat(500, 100)
        self.load_data()
        self.gamestatus = True

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'Retina')
        self.map = Map(path.join(game_folder, 'map.txt'))
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()

    def new(self):
        # set all variables to create a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()

        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                # Spawnpoint
                if tile == 'P':
                    self.player = Player(self, col, row)
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

    # Gitternetz
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        # Game loop - draw
        self.screen.fill(BLACK)
        self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        # pg.draw.rect(self.screen, WHITE, self.player.hit_rect, 2)
        # after drawing everything, flip the window
        pg.display.flip()

    def events(self):
        # Game loop - events
        # Inputs überprüfen
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.gamestatus = False
            elif event.type == pg.KEYDOWN:
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