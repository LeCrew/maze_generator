#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -- Antoine Chiny --

from maze import Maze
import pygame
from pygame.locals import *


class Game:
    def __init__(self, row, col, sprite_size):
        #  Save width and height
        self.width = (col * 2) * sprite_size + sprite_size
        self.height = (row * 2) * sprite_size + sprite_size

        #  Generate new maze
        self.maze = Maze(row, col)
        self.maze.new()

        #  Set sprites size
        self.sprite_size = sprite_size

        #  Initialize pygame module
        pygame.init()
        pygame.display.set_caption("Labyrinthe " + str(col) + "x" + str(row))
        self.window = pygame.display.set_mode((self.width, self.height))

        self.running = True

        #  Load assets
        self.assets = {
            0: pygame.image.load("./assets/wall.png").convert(),
            1: pygame.image.load("./assets/dirt.png").convert()
        }

    #  Display game method
    def display(self):
        for col in range(0, self.width, self.sprite_size):
            self.window.blit(self.assets[0], (0, col))
            self.window.blit(self.assets[0], (col, 0))

        for row in range(self.sprite_size, self.height, self.sprite_size * 2):
            for col in range(self.sprite_size, self.width, self.sprite_size * 2):

                self.window.blit(self.assets[1], (row, col))
                self.window.blit(self.assets[0], (row + self.sprite_size, col + self.sprite_size))

                if not self.maze.cells[row // self.sprite_size // 2][col // self.sprite_size // 2].vet:
                    self.window.blit(self.assets[1], (row, col + self.sprite_size))
                else:
                    self.window.blit(self.assets[0], (row, col + self.sprite_size))

                if not self.maze.cells[row // self.sprite_size // 2][col // self.sprite_size // 2].hor:
                    self.window.blit(self.assets[1], (row + self.sprite_size, col))
                else:
                    self.window.blit(self.assets[0], (row + self.sprite_size, col))
        pygame.display.flip()

    #  Main loop
    def main_loop(self):
        while self.running:
            self.display()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False


if __name__ == '__main__':
    game = Game(20, 20, 32)
    game.main_loop()
