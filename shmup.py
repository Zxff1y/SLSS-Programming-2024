#Shoot 'Em Up

import pygame as pg

# --CONSTANTS--
# COLOURS
WHITE =(255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

WIDTH = 720 Pixels
HEIGHT = 1600
SCREEN_SIZE = (WIDTH, HEIGHT)

def start():
    """Enviroment Setup and Game Loop"""

    pg.init()

    # --Game State Variable--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False 
    clock = pg.time.Clock()

    # All sprites go in thise sprite Group
    all_sprites = pg.sprite.Group()

    pg.display.set_capital("Shoot 'Em Up")

    # --Main Loop--
    while