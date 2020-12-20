from collections import defaultdict, Counter, deque
from dataclasses import dataclass
from functools import cache
import heapq
from itertools import combinations, combinations_with_replacement, groupby, permutations, product, starmap, takewhile
import re

from matplotlib import pyplot as plt
import numpy as np

from aoc import get_input


class MatchError(ValueError):
    pass


def string_to_array(lines):
    arr = np.zeros((len(lines), len(lines[0])), dtype=np.int)
    for r, line in enumerate(lines):
        for c, ch in enumerate(line):
            if ch == '#':
                arr[r, c] = 1
    return arr


def parse_input(input_):
    tiles = {}
    for tile_str in input_.split('\n\n'):
        lines = tile_str.splitlines()
        id = int(re.search(r'\d+', lines[0]).group())

        tile = string_to_array(lines[1:])
        tiles[id] = tile
    return tiles


def available_poses(board):
    available = set()
    for r, c in board:
        available |= {n for n in neighbors((r, c))}
    available -= set(board.keys())
    return available

def neighbors(pos):
    r, c = pos
    yield from [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]


def match(c_pos, candidate, board):
    for n_rot in range(4):
        for flip in (False, True):
            cand = np.rot90(tiles[candidate], k=n_rot)
            cand = np.flip(cand, 1) if flip else cand

            fits_all = True
            for n_pos in [n for n in neighbors(c_pos) if n in board]:
                n_id = board[n_pos]
                neigh = tiles[n_id]

                # if c_pos == (0, 1):
                #     print([n for n in neighbors(c_pos) if n in board])
                #     print(f'{c_pos=}, {n_pos=}, {n_id=}, {n_rot=}, {flip=}, {candidate=}, {n_id=})')

                # find out which edge to check
                c_r, c_c = c_pos
                n_r, n_c = n_pos
                if n_c == c_c + 1 and n_r == c_r:  # neighbor to the right of candidate
                    fits = np.array_equal(cand[:, -1], neigh[:, -0])
                elif n_c == c_c - 1 and n_r == c_r:  # neighbor to the left of candidate
                    fits = np.array_equal(cand[:, 0], neigh[:, -1])
                elif n_c == c_c and n_r == c_r + 1:  # neighbor above candidate
                    fits = np.array_equal(cand[0, :], neigh[-1, :])
                    # if c_pos == (0, 1):
                    #     print('cand', cand[0, :])
                    #     print('neigh', neigh[-1, :])
                elif n_c == c_c and n_r == c_r - 1:  # neighbor below candidate
                    fits = np.array_equal(cand[-1, :], neigh[0, :])
                else:
                    raise Exception(f'Wtf iets is gruwelijk mis. {candidate=}, {c_pos=}, {n_pos=}')

                if not fits:
                    fits_all = False
                    break
            if fits_all:
                return cand
    else:
        raise MatchError

def edge_points(coords):
    min_r = min(r for r, c in coords)
    max_r = max(r for r, c in coords)
    min_c = min(c for r, c in coords)
    max_c = max(c for r, c in coords)
    return min_r, max_r, min_c, max_c


def solve(tiles):
    queue = deque(id for id in tiles)
    board = {(0, 0): queue.popleft()}
    while queue:
        candidate = queue.popleft()
        #
        # print('#' * 80)
        # print(len(queue))
        # print(f'{candidate=}')
        # print(f'{board=}')

        for av_pos in available_poses(board):
            # print(f'{av_pos=}')
            try:
                cand_transformed = match(av_pos, candidate, board)
                tiles[candidate] = cand_transformed
                board[av_pos] = candidate
                break
            except MatchError:
                continue
        else:
            # did not fit anywhere, put in the back of the queue
            queue.append(candidate)
    return board


# 20-1 test
with open('input/20-1-test.txt') as f:
    tiles = parse_input(f.read())
board = solve(tiles)
min_r, max_r, min_c, max_c = edge_points(board)
assert board[(min_r, min_c)] * board[(max_r, min_c)] * board[(min_r, max_c)] * board[(max_r, max_c)] == 20899048083289

# 20-1
tiles = parse_input(get_input(day=20, as_list=False))
board = solve(tiles)
print(board)
min_r, max_r, min_c, max_c = edge_points(board)
print(board[(min_r, min_c)] * board[(max_r, min_c)] * board[(min_r, max_c)] * board[(max_r, max_c)])


L = 12
im_size = 8
image = np.zeros((L*im_size, L*im_size))
for r in range(L):
    for c in range(L):
        tile = tiles[board[(min_r + r, min_c + c)]]

        R, C = r * im_size, c * im_size
        image[R:R+im_size, C:C+im_size] = tile[1:-1, 1:-1]

plt.imshow(image)
plt.show()

# 20-2 test
sea_monster = string_to_array('''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''.splitlines())
with open('input/20-2-test.txt') as f:
    image = string_to_array(f.read().splitlines())
plt.imshow(image)
plt.show()
