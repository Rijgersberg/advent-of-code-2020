from collections import deque
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
        id_line, *tile_lines = tile_str.splitlines()

        id = int(re.search(r'\d+', id_line).group())
        tile = string_to_array(tile_lines)
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

                # find out which edge to check
                c_r, c_c = c_pos
                n_r, n_c = n_pos
                if n_c == c_c + 1 and n_r == c_r:  # neighbor to the right of candidate
                    fits = np.array_equal(cand[:, -1], neigh[:, -0])
                elif n_c == c_c - 1 and n_r == c_r:  # neighbor to the left of candidate
                    fits = np.array_equal(cand[:, 0], neigh[:, -1])
                elif n_c == c_c and n_r == c_r + 1:  # neighbor below candidate
                    fits = np.array_equal(cand[-1, :], neigh[0, :])
                elif n_c == c_c and n_r == c_r - 1:  # neighbor above candidate
                    fits = np.array_equal(cand[0, :], neigh[-1, :])
                else:
                    raise ValueError

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
        candidate_id = queue.popleft()

        for av_pos in available_poses(board):
            try:
                cand_transformed = match(av_pos, candidate_id, board)
                tiles[candidate_id] = cand_transformed
                board[av_pos] = candidate_id
                break
            except MatchError:
                continue
        else:
            # did not fit anywhere, put in the back of the queue
            queue.append(candidate_id)
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
min_r, max_r, min_c, max_c = edge_points(board)
print(board[(min_r, min_c)] * board[(max_r, min_c)] * board[(min_r, max_c)] * board[(max_r, max_c)])


def stitch(tiles, board, L, im_size):
    image = np.zeros((L*im_size, L*im_size), dtype=np.int)
    for r in range(L):
        for c in range(L):
            tile = tiles[board[(min_r + r, min_c + c)]]

            R, C = r * im_size, c * im_size
            image[R:R+im_size, C:C+im_size] = tile[1:-1, 1:-1]
    return image


# 20-2 test
def count_seamonsters(orig_image, monster):
    count = 0
    for n_rot in range(4):
        for flip in (False, True):
            image = np.rot90(orig_image, k=n_rot)
            image = np.flip(image, 1) if flip else image

            L_image, W_image = image.shape
            L_monster, W_monster = monster.shape

            for i in range(L_image-L_monster):
                for j in range(W_image-W_monster):
                    # check if for every 1 in the monster there is a 1 in the image slice
                    if np.array_equal(monster & image[i:i+L_monster, j:j+W_monster], monster):
                        count += 1
    return count

sea_monster = string_to_array('''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''.splitlines())
with open('input/20-2-test.txt') as f:
    test_image = string_to_array(f.read().splitlines())
plt.imshow(test_image)
plt.show()

count = count_seamonsters(test_image, sea_monster)
assert count == 2
assert test_image.sum() - count * sea_monster.sum() == 273

# 20-2
puzzle_image = stitch(tiles, board, L=12, im_size=8)
plt.imshow(puzzle_image)
plt.show()
count = count_seamonsters(puzzle_image, sea_monster)
print(puzzle_image.sum() - count * sea_monster.sum())
