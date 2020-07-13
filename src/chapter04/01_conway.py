#! /usr/bin/env python3
# Conway's Game of Life
import copy
import random
import time


def create_cells(width, height):
    cells = []
    for x in range(width):
        column = []  # Create a new column.
        for y in range(height):
            if random.randint(0, 1) == 0:
                column.append("#")  # Add a living cell.
            else:
                column.append(" ")  # Add a dead cell.
        cells.append(column)
    return cells


def print_cells(cells, width, height):
    print("\n\n\n\n\n")  # Separate each step with newlines.
    print("*" * 60 + "\n")
    for y in range(height):
        for x in range(width):
            print(cells[x][y], end='')  # Print the # or space.
        print()  # Print a newline at the end of the row.


def calculate_neighbors(cells, x, y, width, height):
    left = (x - 1) % width
    right = (x + 1) % width
    above = (y - 1) % height
    below = (y + 1) % height

    # Count number of living neighbors:
    neighbors = 0
    if cells[left][above] == '#':
        neighbors += 1  # Top-left neighbor is alive.
    if cells[x][above] == '#':
        neighbors += 1  # Top neighbor is alive.
    if cells[right][above] == '#':
        neighbors += 1  # Top-right neighbor is alive.
    if cells[left][y] == '#':
        neighbors += 1  # Left neighbor is alive.
    if cells[right][y] == '#':
        neighbors += 1  # Right neighbor is alive.
    if cells[left][below] == '#':
        neighbors += 1  # Bottom-left neighbor is alive.
    if cells[x][below] == '#':
        neighbors += 1  # Bottom neighbor is alive.
    if cells[right][below] == '#':
        neighbors += 1  # Bottom-right neighbor is alive.
    return neighbors


def is_gonna_live(cell, neighbors):
    return (cell == '#' and (neighbors == 2 or neighbors == 3)) or (cell == ' ' and neighbors == 3)


WIDTH = 60
HEIGHT = 20
next_cells = create_cells(WIDTH, HEIGHT)

while True:  # Main program loop.

    current_cells = copy.deepcopy(next_cells)
    print_cells(current_cells, WIDTH, HEIGHT)
    for x in range(WIDTH):
        for y in range(HEIGHT):
            neighbors = calculate_neighbors(current_cells, x, y, WIDTH, HEIGHT)

            if is_gonna_live(current_cells[x][y], neighbors):
                next_cells[x][y] = '#'
            else:
                next_cells[x][y] = ' '
    time.sleep(1)  # Add a 1-second pause to reduce flickering.
