#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -- Antoine Chiny --

from maze import Maze
import pygame
from pygame.locals import *

if __name__ == '__main__':
    running = True
    new_maze = Maze(10, 10)
    pygame.init()
    window = pygame.display.set_mode((1080, 720))

    while running:
        window.blit()
