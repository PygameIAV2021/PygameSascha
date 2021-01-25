# Welcome to Tanks!

by Sascha. With Pygame. Inspired by KidsCanCode from YouTube.

## Requirements:

You need Python for this game and it should be the Version 3.8 or higher.
The script was tested on **Pyhon 3.8** with **pygame** version **2.0**.

# Running instructions:

To play the game run **python tanks.py**.
After that you can follow the instructions from the game.

## Instructions:

The game called Tanks. You play a tank against other tanks. It is a **tiled-based topdown shooter** like bomberman.
The goal of the game is to survive and shoot all enemy tanks before they can kill you.
Enemy tanks can hit you and you loose 10 damage from healthbar. Overall you have 100 Points on your healthbar.

## Controlling:

- left arrow or a = move left
- right arrow or d = move right
- up arrow or w = move forward
- down arrow or s = move backward
- space = shooting

If you hold the spacebar, you shot while you holding it.
In the game are three different weapon mods.

Test it to find it out.
**Have fun!**

## Technical details:

The gamewindow is actually set. You can change it in the `settings.py`.
If you want you can change the frame rate (FPS) in the `settings.py` too.
The map was created with mapeditor

## Libraries:

I used the followed Libraries below:

- pygame
  - to program the game
- math
  - to locate players angle
- random
  - to generate numbers
- sys
  - to get system parameters
- pytweening
  - to generate easing functions
- pytmx
  - to include .tmx maps
- itertools
  - to iterate easy in loops
- os
  - to match data pathway

# Credits:

In my game i used characters and images from **KidsCanCode** from Youtube.
> https://github.com/kidscancode/pygame_tutorials/tree/master/tilemap/working

The map was created with a ***mapeditor***
> https://www.mapeditor.org/



