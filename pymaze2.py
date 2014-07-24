#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Written by phoemur - jul/2014
# Thanks to Joe Wingbermuehle whoose maze generator
# ( https://raw.github.com/joewing/maze ) I was based on
#

import pygame
import sys
import random

from pygame.locals import *

FPS = 10
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
BOXSIZE = 30

# The size of the maze (must be odd).
WIDTH = 25
HEIGHT = 19
assert WIDTH % 2 != 0, 'The side must be odd'
assert HEIGHT % 2 != 0, 'The side must be odd'

XMARGIN = int(WINDOWWIDTH - (WIDTH * BOXSIZE)) / 2
YMARGIN = int(WINDOWHEIGHT - (HEIGHT * BOXSIZE)) / 2

# Colors  R    G    B
WHITE = (255, 255, 255)
BLACK = (0,   0,   0)

# The maze.
MAZE = dict()


# Initialize the maze.
def init_maze():
    for x in range(0, WIDTH):
        MAZE[x] = dict()
        for y in range(0, HEIGHT):
            MAZE[x][y] = 1


# Carve the maze starting at x, y.
def carve_maze(x, y):
    dir = random.randint(0, 3)
    count = 0
    while count < 4:
        dx = 0
        dy = 0
        if dir == 0:
            dx = 1
        elif dir == 1:
            dy = 1
        elif dir == 2:
            dx = -1
        else:
            dy = -1
        x1 = x + dx
        y1 = y + dy
        x2 = x1 + dx
        y2 = y1 + dy
        if x2 > 0 and x2 < WIDTH and y2 > 0 and y2 < HEIGHT:
            if MAZE[x1][y1] == 1 and MAZE[x2][y2] == 1:
                MAZE[x1][y1] = 0
                MAZE[x2][y2] = 0
                carve_maze(x2, y2)
        count = count + 1
        dir = (dir + 1) % 4


# Generate the maze.
def generate_maze():
    random.seed()
    MAZE[1][1] = 0
    carve_maze(1, 1)
    MAZE[1][0] = 0
    MAZE[WIDTH - 2][HEIGHT - 1] = 0


def get_badguy_init():
    pos = [random.randint(1, WIDTH - 1), HEIGHT - 2]
    while MAZE[pos[0]][HEIGHT - 2] != 0:
        pos = [random.randint(1, WIDTH - 1), HEIGHT - 2]

    return pos


def get_badguy_way():
    possible = ['left',
                'right',
                'down',
                'up']
    random.shuffle(possible)
    return possible[random.randint(0, len(possible) - 1)]


def main():
    global FPSCLOCK, DISPLAYSURF, MAZE
    init_maze()
    generate_maze()

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('PyMaze 2.0')
    brickImg = pygame.image.load('brick.jpg')
    pacImg = pygame.image.load('pac.png')
    pacbadImg = pygame.image.load('pac_bad.png')
    floorImg = pygame.image.load('floor.jpg')

    # good guy init
    good_direction = None
    good_x = 1
    good_y = 0

    # bad guy init
    bad_direction = 'left'
    bad_x, bad_y = get_badguy_init()

    # Mainloop
    while True:
        # Print the Maze
        DISPLAYSURF.fill(BLACK)
        for y in range(0, HEIGHT):
            for x in range(0, WIDTH):
                if MAZE[x][y] != 0:
                    DISPLAYSURF.blit(
                        brickImg, ((x * BOXSIZE) + XMARGIN,
                                   (y * BOXSIZE) + YMARGIN))
                else:
                    DISPLAYSURF.blit(
                        floorImg, ((x * BOXSIZE) + XMARGIN,
                                   (y * BOXSIZE) + YMARGIN))

        # Event Handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                if event.key in (K_LEFT, K_a):
                    good_direction = 'left'
                elif event.key in (K_RIGHT, K_d):
                    good_direction = 'right'
                elif event.key in (K_UP, K_w):
                    good_direction = 'up'
                elif event.key in (K_DOWN, K_s):
                    good_direction = 'down'

        # Check win
        if good_y == HEIGHT - 1:
            break
        if bad_y == HEIGHT - 1:
            bad_y -= 1
            bad_direction = 'left'

        # Check Loose
        if (good_x, good_y) == (bad_x, bad_y):
            break

        # Good Guy movement
        if good_direction == 'left':
            if 0 < good_x <= WIDTH:
                if MAZE[good_x - 1][good_y] != 1:
                    good_x -= 1
                else:
                    good_direction = None
            else:
                good_direction = None
        elif good_direction == 'right':
            if 0 <= good_x < WIDTH:
                if MAZE[good_x + 1][good_y] != 1:
                    good_x += 1
                else:
                    good_direction = None
            else:
                good_direction = None
        elif good_direction == 'up':
            if 0 < good_y <= HEIGHT:
                if MAZE[good_x][good_y - 1] != 1:
                    good_y -= 1
                else:
                    good_direction = None
            else:
                good_direction = None
        elif good_direction == 'down':
            if 0 <= good_y < HEIGHT:
                if MAZE[good_x][good_y + 1] != 1:
                    good_y += 1
                else:
                    good_direction = None
            else:
                good_direction = None

        DISPLAYSURF.blit(
            pacImg, ((good_x * BOXSIZE) + XMARGIN,
                     (good_y * BOXSIZE) + YMARGIN))

        # Bad Guy movement
        if bad_direction == 'left':
            if 0 < bad_x <= WIDTH:
                if MAZE[bad_x - 1][bad_y] != 1:
                    bad_x -= 1
                else:
                    bad_direction = get_badguy_way()
            else:
                bad_direction = get_badguy_way()
        elif bad_direction == 'right':
            if 0 <= bad_x < WIDTH:
                if MAZE[bad_x + 1][bad_y] != 1:
                    bad_x += 1
                else:
                    bad_direction = get_badguy_way()
            else:
                bad_direction = get_badguy_way()
        elif bad_direction == 'up':
            if 0 < bad_y <= HEIGHT:
                if MAZE[bad_x][bad_y - 1] != 1:
                    bad_y -= 1
                else:
                    bad_direction = get_badguy_way()
            else:
                bad_direction = get_badguy_way()
        elif bad_direction == 'down':
            if 0 <= bad_y < HEIGHT:
                if MAZE[bad_x][bad_y + 1] != 1:
                    bad_y += 1
                else:
                    bad_direction = get_badguy_way()
            else:
                bad_direction = get_badguy_way()

        DISPLAYSURF.blit(
            pacbadImg, ((bad_x * BOXSIZE) + XMARGIN,
                        (bad_y * BOXSIZE) + YMARGIN))

        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
