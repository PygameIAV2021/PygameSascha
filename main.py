# Project Pygame in SKP

import pygame
import random
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
        self.gamestatus = True

    def new(self):
        # Start a new game
        self.all_sprites = pg.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.run()

    def run(self):
        # Game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

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