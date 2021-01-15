import pygame as pg
vec = pg.math.Vector2
# settings.py

TITLE = " PyGame!"

WALL_IMG = 'tileGrass1.png'
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
BARREL_OFFSET = vec(18, 0)
# Gun settings
BULLET_IMG = 'bulletBlue3.png'
BULLET_SPEED = 200
BULLET_LIFETIME = 1000
BULLET_RATE = 150
KICKBACK = 200
GUN_SPREAD = 5

# Mob settings
MOB_IMG = 'tank_dark.png'
MOB_SPEED = 150
MOB_HIT_RECT = pg.Rect(0, 0, 35, 35)

# Colors
BLACK   =   ( 0, 0, 0)
WHITE   =   ( 255, 255, 255)
RED     =   ( 255, 0, 0)
GREEN   =   ( 0, 255, 0)
BLUE    =   ( 0, 0, 255)
YELLOW  =   (255, 255, 0)
LIGHTGREY = (100, 100, 100)
BROWN =     (106, 55, 5)
BGCOLOR = BROWN

