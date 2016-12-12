#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -- Antoine Chiny --

# Maze generator => backtracking algorithm

from random import randint, choice


class Cell:
    def __init__(self):
        self.visited = False
        self.vet = True
        self.hor = True


class Pt:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Maze:
    def __init__(self, row, col):
        self.width = col
        self.height = row
        self.cells = [[Cell() for x in range(col)] for y in range(row)]
        self.possible_factor = [Pt(0, -1), Pt(1, 0), Pt(0, 1), Pt(-1, 0)]
        self.new()

    def is_any_unvisited_cells(self):
        for row in self.cells:
            for col in row:
                if not col.visited:
                    return True
        return False

    def display(self):
        print '##'*self.width + '#'
        for row in self.cells:
            current_line = "#"
            for col in row:
                if not col.vet:
                    current_line += '  '
                else:
                    current_line += ' #'
            current_line += '\n#'
            for col in row:
                if not col.hor:
                    current_line += ' #'
                else:
                    current_line += '##'
            print current_line

    def random_cell(self):
        return Pt(randint(0, self.width-2), randint(0, self.height-2))

    def has_any_neighbours(self, x, y):
        neighbours_list = []
        for factor in self.possible_factor:
            if 0 <= x+factor.x < self.width and 0 <= y+factor.y < self.height:
                if not self.cells[y+factor.y][x+factor.x].visited:
                    neighbours_list.append(Pt(x+factor.x, y+factor.y))
        return neighbours_list

    def new(self):
        cells_stack = []
        current_cell = self.random_cell()

        self.cells[current_cell.y][current_cell.x].visited = True

        while self.is_any_unvisited_cells():
            valid_neighbours = self.has_any_neighbours(current_cell.x, current_cell.y)

            if len(valid_neighbours) > 0:
                select_neighbour = choice(valid_neighbours)
                cells_stack.append(current_cell)

                if current_cell.x-1 == select_neighbour.x or current_cell.y-1 == select_neighbour.y:
                    if current_cell.y == select_neighbour.y:
                        self.cells[select_neighbour.y][select_neighbour.x].vet = False
                    else:
                        self.cells[select_neighbour.y][select_neighbour.x].hor = False
                else:
                    if current_cell.y == select_neighbour.y:
                        self.cells[current_cell.y][current_cell.x].vet = False
                    else:
                        self.cells[current_cell.y][current_cell.x].hor = False
                current_cell = select_neighbour
                self.cells[current_cell.y][current_cell.x].visited = True
            else:
                current_cell = cells_stack.pop()