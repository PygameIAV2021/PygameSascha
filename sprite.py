# Sprite classes for main.py
import pygame as pg
import random
from settings import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((30, 40))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        # self.rect.x = random.randrange(WIDTH - self.rect.width)
        # self.rect.bottom = HEIGHT - 50
        self.rect.x = x
        self.rect.y = y

        self.change_x = 0
        self.change_y = 0

    def move(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                self.change_x = -SPEED
            elif event.key == pg.K_RIGHT:
                self.change_x = SPEED
            elif event.key == pg.K_SPACE:
                self.change_y = JUMP_POWER

    def update(self):
        self.rect = self.rect.move(self.change_x, 0)
        self.rect.x += self.change_x


        # self.rect.x += self.x
        # self.rect.y += self.y

    # def shoot(self):
        # bullet = Bullet(self.rect.centerx, self.rect.top)
        # all_sprites.add(bullet)
        # bullets.add(bullet)

class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((10, 10))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.y = -10

    def update(self):
        self.rect.y += self.y

        if self.rect.bottom < 0:
            self.kill()

class Wall(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y