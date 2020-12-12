from collections import defaultdict, Counter, deque
from dataclasses import dataclass
import heapq
from itertools import combinations, combinations_with_replacement, permutations, product
import re
from math import cos, sin, pi, sqrt

from aoc import get_input


instructions = [(i[0], int(i[1:])) for i in get_input(day=12)]

mappings = {'N': (0, 1),
            'S': (0, -1),
            'E': (1, 0),
            'W': (-1, 0),
            'L': 1,
            'R': -1}

def move(action, value, pos, direc):
    if action in 'NSEW':
        nx = pos[0] + value * mappings[action][0]
        ny = pos[1] + value * mappings[action][1]
        pos = nx, ny
    elif action == 'L':
        direc = (direc + value) % 360
    elif action == 'R':
        direc = (direc - value) % 360
    elif action in 'F':
        nx = pos[0] + int(round(cos(direc / 360 * 2 * pi))) * value
        ny = pos[1] + int(round(sin(direc / 360 * 2 * pi))) * value
        pos = nx, ny
    else:
        raise ValueError
    return pos, direc

# 12-1
pos = (0, 0)
direc = 0
for action, value in instructions:
    pos, direc = move(action, value, pos, direc)

print(abs(pos[0]) + abs(pos[1]))

# 12-2
def move2(action, value, wp, pos):
    if action in 'NSEW':
        nwx = wp[0] + value * mappings[action][0]
        nwy = wp[1] + value * mappings[action][1]
        wp = nwx, nwy
    elif action in 'LR':
        if action == 'R':
            value = -value % 360

        if value == 0:
            pass
        elif value == 90:
            wp = -wp[1], wp[0]
        elif value == 180:
            wp = -wp[0], -wp[1]
        elif value == 270:
            wp = wp[1], -wp[0]
        else:
            raise ValueError
    elif action in 'F':
        pos = pos[0] + wp[0] * value, pos[1] + wp[1] * value
    else:
        raise ValueError
    return wp, pos


pos = (0, 0)
wp = (10, 1)
for action, value in instructions:
    wp, pos = move2(action, value, wp, pos)

print(abs(pos[0]) + abs(pos[1]))
