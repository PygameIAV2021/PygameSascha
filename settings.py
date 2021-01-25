# settings.py

import pygame as pg
vec = pg.math.Vector2

TITLE = " PyGame!"
WALL_IMG = 'tileGrass1.png'
MAPBG_IMG = 'mapbg.png'

# Display Surface
WIDTH = 896
HEIGHT = 640
HSW = WIDTH / 2
HSH = HEIGHT / 2
TILESIZE = 64
GRIDWITDH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE
FPS = 60

# Player settings
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'tank_blue.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
BARREL_OFFSET = vec(18, 0)
PLAYER_HEALTH = 100

# Weapon settings
BULLET_IMG = 'tilebullet.png'
## Weapon dictionary
WEAPONS = {}
WEAPONS['singleshot'] = {'bullet_speed': 500,
                         'bullet_lifetime': 1000,
                         'rate': 250,
                         'kickback': 200,
                         'spread': 5,
                         'damage': 10,
                         'bullet_size': 'lg',
                         'bullet_count': 1}
WEAPONS['shotgun'] = {'bullet_speed': 400,
                       'bullet_lifetime': 500,
                       'rate': 900,
                       'kickback': 300,
                       'spread': 20,
                       'damage': 5,
                       'bullet_size': 'sm',
                       'bullet_count': 12}
WEAPONS['minigun'] = {'bullet_speed': 600,
                       'bullet_lifetime': 800,
                       'rate': 50,
                       'kickback': 150,
                       'spread': 3,
                       'damage': 5,
                       'bullet_size': 'sm',
                       'bullet_count': 1}

# Mob settings
MOB_IMG = 'tank_dark.png'
SPLAT_IMG = 'oilSpill_large.png'
MOB_SPEEDS = [150, 100, 75, 125, 150]
MOB_HIT_RECT = pg.Rect(0, 0, 35, 35)
MOB_HEALTH = 100
MOB_DAMAGE = 10
MOB_KNOCKBACK = 20
AVOID_RADIUS = 50
DETECT_RADIUS = 500

# Effects
EXPLOSION = ['explosion00.png', 'explosion01.png', 'explosion02.png', 'explosion03.png',
             'explosion04.png', 'explosion05.png', 'explosion06.png', 'explosion07.png',
             'explosion08.png']
FLASH_DURATION = 40
DAMAGE_ALPHA = [i for i in range(0, 255, 25)]
NIGHT_COLOR = (30, 30, 30)
LIGHT_RADIUS = (500, 500)
LIGHT_MASK = 'light_350_med.png'

# Layers
WALL_LAYER = 1
PLAYER_LAYER = 2
BULLET_LAYER = 3
MOB_LAYER = 2
EFFECTS_LAYER = 4
ITEM_LAYER = 1

# Items
ITEM_IMAGES = {'health': 'healthitem.png',
               'shotgun': 'tankDark_barrel3_outline.png',
               'minigun': 'tankDark_barrel3_outline.png'}
HEALTH_PACK_AMOUNT = 20
BOB_RANGE = 15
BOB_SPEED = 0.4

# Sounds
BG_MUSIC = 'Blazer_Rail.wav'
WEAPON_SOUNDS = {'singleshot': ['singleshot.wav'],
                 'shotgun': ['shotgun.wav'],
                 'minigun': ['singleshot.wav']}
PLAYER_HIT_SOUNDS = ['8.wav', '9.wav', '10.wav', '11.wav', '12.wav', '13.wav', '14.wav']
ENEMY_HIT_SOUNDS = ['splat-15.wav']
ENEMY_SOUNDS = ['Tank.wav']
EFFECT_SOUNDS = {'level_start': 'level_start.wav',
                 'health_up': 'health_pack.wav',
                 'gun_pickup': 'health_pack.wav'}

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

