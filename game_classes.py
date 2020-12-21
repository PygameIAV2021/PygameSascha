import pygame, sys, random, string, math
from settings import *

class SpriteSheet:
    def __init__(self, image_path):
        self.sprite_sheet = pygame.image.load(image_path).convert()

    def get_image(self, x, y, width, height):
        image = pygame.Surface((width, height))
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        return image

class player(pygame.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        self.image = self.game.SpriteSheet.get_image(14, 14, 34, 46)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)