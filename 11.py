from collections import defaultdict, Counter, deque
from dataclasses import dataclass
import heapq
from itertools import combinations, combinations_with_replacement, permutations, product
import re

import copy

from aoc import get_input

# game of ~life~ thrones.
game_str = get_input(day=11)
N, M = len(game_str[0]), len(game_str)

game = {x: [None] * M for x in range(N)}
for y, line in enumerate(game_str):
    for x, c in enumerate(line):
        game[x][y] = c

original_game = copy.deepcopy(game)

# 11-1
def neighbors(x, y):
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if not (i, j) == (x, y) and 0 <= i < N and 0 <= j < M:
                yield i, j

def update(old_game):
    game = copy.deepcopy(old_game)
    for x in range(N):
        for y in range(M):
            seat = game[x][y]
            if seat != '.':
                adj_seats = sum(old_game[i][j] == '#' for i, j in neighbors(x, y))
                if seat == 'L':
                    if adj_seats == 0:
                        game[x][y] = '#'
                elif seat == '#':
                    if adj_seats >= 4:
                        game[x][y] = 'L'
    return game

t = 0
while True:
    t += 1
    new_game = update(copy.deepcopy(game))
    if new_game == game:
        break
    game = new_game

print(t)
print(sum(sum([c == '#' for c in row]) for row in game.values()))


# 11-2
def search(x, y, dir, game):
    new_x, new_y = x + dir[0], y + dir[1]
    if 0 <= new_x < N and 0 <= new_y < M:
        c = game[new_x][new_y]
        if c in ['L', '#']:
            return new_x, new_y
        else:
            return search(new_x, new_y, dir, game)
    else:
        return None

def make_visible_neighbors(game):
    neighbor_lookup = {}
    for x in range(N):
        for y in range(M):
            directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
            neighbors = []
            for dir in directions:
                neighbor = search(x, y, dir, game)
                if neighbor is not None:
                    neighbors.append(neighbor)
            neighbor_lookup[(x, y)] = neighbors
    return neighbor_lookup

def update(old_game):
    game = copy.deepcopy(old_game)
    for x in range(N):
        for y in range(M):
            seat = game[x][y]
            if seat != '.':
                adj_seats = sum(old_game[i][j] == '#' for i, j in visible_neighbors[(x, y)])
                if seat == 'L':
                    if adj_seats == 0:
                        game[x][y] = '#'
                elif seat == '#':
                    if adj_seats >= 5:
                        game[x][y] = 'L'
    return game

visible_neighbors = make_visible_neighbors(original_game)
game = original_game
t = 0
while True:
    t += 1
    new_game = update(copy.deepcopy(game))
    if new_game == game:
        break
    game = new_game

print(t)
print(sum(sum([c == '#' for c in row]) for row in game.values()))


