# settings.py
# Feste Parameter für Pygame, Bibliotheken

import pygame as pg
import os, sys, random, string, time, argparse
from math import cos, sin, pi as PI
from pygame.locals import *
from game_classes import *

TITLE = " Worms for you"

# Display Oberfläche
WIDTH = 640
HEIGHT = 480
HSW = WIDTH / 2
HSH = HEIGHT / 2
AREA = WIDTH * HEIGHT

# FPS
FPS = 1

# Colors
BLACK   = ( 0, 0, 0)
WHITE   = ( 255, 255, 255)
RED     = ( 255, 0, 0)
GREEN   = ( 0, 255, 0)
BLUE    = ( 0, 0, 255)
