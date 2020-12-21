# defaults.py
# Feste Parameter für Pygame, Bibliotheken

import pygame, os, sys, random, string, time, argparse
from math import cos, sin, pi as PI
from pygame.locals import *
from game_classes import *

# Display Oberfläche
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
HSW = SCREEN_WIDTH / 2
HSH = SCREEN_HEIGHT / 2
AREA = SCREEN_WIDTH * SCREEN_HEIGHT

# FPS
FPS = 1

# Farben
BLACK   = ( 0, 0, 0)
WHITE   = ( 255, 255, 255)
RED     = ( 255, 0, 0)
GREEN   = ( 0, 255, 0)
BLUE    = ( 0, 0, 255)
