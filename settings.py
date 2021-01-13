import pygame as pg
# settings.py

TITLE = " PyGame!"

# Display Surface
WIDTH = 864
HEIGHT = 608
HSW = WIDTH / 2
HSH = HEIGHT / 2
FPS = 60
TILESIZE = 64
GRIDWITDH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player settings
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'tank_blue.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)

# Colors
BLACK   = ( 0, 0, 0)
WHITE   = ( 255, 255, 255)
RED     = ( 255, 0, 0)
GREEN   = ( 0, 255, 0)
BLUE    = ( 0, 0, 255)
YELLOW  = (255, 255, 0)
LIGHTGREY = (100, 100, 100)

