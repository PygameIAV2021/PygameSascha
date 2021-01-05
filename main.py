# Project Pygame in SKP

import pygame
import random
import sys
from settings import *
from sprite import *

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
        pass

    def new(self):
        # Start a new game
        self.all_sprites = pg.sprite.Group()

        self.walls = pg.sprite.Group()

        floor_block = Wall(0, HEIGHT - 10, WIDTH, 10)
        right_block = Wall(WIDTH - 10, 0, 10, HEIGHT)
        left_block = Wall(0, 0, 10, HEIGHT)

        self.all_sprites.add(floor_block, right_block, left_block)
        self.walls.add(floor_block, right_block, left_block)

        self.player = Player(self, 300, 300)


        # self.bullets = pg.sprite.Group()
        # self.mob = Mob()
        # self.all_sprites.add(self.mob)



        # self.bullet = Bullet()
        # self.all_sprites.add(self.bullet)
        # self.bullets.add(self.bullet)

        self.run()

    def run(self):
        # Game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # Game loop - update
        self.all_sprites.update()

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
                # if event.type == pg.K_SPACE:
                    # self.player.shoot()

    def draw(self):
        # Game loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # after drawing everything, flip the window
        pg.display.flip()

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