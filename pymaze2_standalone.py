#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file has all media embedded for standalone use
# Should use the other file (pymaze2.py) whenever possible

import pygame
import sys
import random
import base64

from io import BytesIO
from pygame.locals import *

# brick.jpg
BRICK = b'''
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
'''

# floor.jpg
FLOOR = b'''
/9j/4AAQSkZJRgABAQEASABIAAD//gA7Q1JFQVRPUjogZ2QtanBlZyB2MS4wICh1c2luZyBJSkcg
SlBFRyB2NjIpLCBxdWFsaXR5ID0gOTAK/9sAQwADAgIDAgIDAwMDBAMDBAUIBQUEBAUKBwcGCAwK
DAwLCgsLDQ4SEA0OEQ4LCxAWEBETFBUVFQwPFxgWFBgSFBUU/9sAQwEDBAQFBAUJBQUJFA0LDRQU
FBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQU/8IAEQgAHgAg
AwERAAIRAQMRAf/EABgAAQEBAQEAAAAAAAAAAAAAAAABAgMG/8QAFwEBAQEBAAAAAAAAAAAAAAAA
AAECBv/aAAwDAQACEAMQAAAB9PwXWXQTNyasGZRdQTN6I2DD/8QAGxAAAgIDAQAAAAAAAAAAAAAA
AjEAAQMRIRD/2gAIAQEAAQUCOKnQRnrmuI0dqkzye45//8QAFxEAAwEAAAAAAAAAAAAAAAAAAAEQ
Qf/aAAgBAwEBPwFVmXDLgqz/xAAYEQEBAQEBAAAAAAAAAAAAAAAAARARAv/aAAgBAgEBPwFF2Kme
Vzjixx//xAAXEAADAQAAAAAAAAAAAAAAAAAAAhAB/9oACAEBAAY/AhB7htUaoPP/xAAfEAEAAgIB
BQEAAAAAAAAAAAABABEhYbExQVFx8KH/2gAIAQEAAT8heUG8PBOqvvOqvvHkFrBwytvxLU+Flvaj
K0/Mcud8QU22C22Qac75gW/TwQGhsiNDbA/hwz//2gAMAwEAAgADAAAAELNM3xaHg//EABsRAAMA
AwEBAAAAAAAAAAAAAAABMRARQVHw/9oACAEDAQE/EIPTwjB6FhRWyaIGH37gnBj/xAAaEQADAAMB
AAAAAAAAAAAAAAAAAREhMUHw/9oACAECAQE/EHRrgaVCrHhweMevBk4PZFJotjCie6bPdEP/xAAf
EAEBAQACAQUBAAAAAAAAAAABEQAhYTFBUXGR8KH/2gAIAQEAAT8QJQr28LdTCIes1iorAfS4hCvb
4wKl8pU6GVFCn6cCDH+k5VL5Sh0M6GoV8RZeUBLjtuXkEC56bqAhSPiLAUnLn47ymIhQnmuERCoE
8YgROHfx1v/Z
'''

# pac.png
PAC = b'''
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
uhPgkgAAAABJRU5ErkJggg==
'''

# pac_bad.png
PAC_BAD = b'''
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
'''

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

# Directions
POSSIBLE = ('left',
            'right',
            'down',
            'up')


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
    return random.choice(POSSIBLE)


def main():
    global FPSCLOCK, DISPLAYSURF, MAZE
    init_maze()
    generate_maze()

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('PyMaze 2.0')

    with BytesIO(base64.decodestring(BRICK)) as fh:
        brickImg = pygame.image.load(fh)

    with BytesIO(base64.decodestring(PAC)) as fh:
        pacImg = pygame.image.load(fh)

    with BytesIO(base64.decodestring(PAC_BAD)) as fh:
        pacbadImg = pygame.image.load(fh)

    with BytesIO(base64.decodestring(FLOOR)) as fh:
        floorImg = pygame.image.load(fh)

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
