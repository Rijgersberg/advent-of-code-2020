from collections import defaultdict
from copy import deepcopy

from aoc import get_input

DIRECTIONS = {'e': 2, 'se': 1 - 2j, 'sw': -1 - 2j, 'w': -2, 'nw': -1 + 2j, 'ne': 1 + 2j}


class TraversalError(ValueError):
    pass


def parse(string):
    if string == '':
        return []

    if string[0] not in DIRECTIONS:
        if string[:2] in DIRECTIONS:
            return [DIRECTIONS[string[:2]]] + parse(string[2:])
        else:
            raise TraversalError(f'Next two letters of string "{string}" not in DIRECTIONS')
    else:
        if string[:2] not in DIRECTIONS:
            return [DIRECTIONS[string[0]]] + parse(string[1:])
        else:  # both the next letter by itself and the next two letters are valid instructions
            try:
                return [DIRECTIONS[string[0]]] + parse(string[1:])
            except TraversalError:
                return [DIRECTIONS[string[:2]]] + parse(string[2:])


def flip(positions):
    floor = defaultdict(bool)

    for pos in positions:
        floor[pos] = not floor[pos]
    return floor


# 24-1
with open('input/24-1-test.txt') as f:
    test_positions = [sum(parse(line)) for line in f.read().splitlines()]
assert sum(flip(test_positions).values()) == 10

positions = [sum(parse(line)) for line in get_input(day=24)]
print(sum(flip(positions).values()))


# 24-2
def neighbors(pos):
    yield from (pos + vec for vec in DIRECTIONS.values())


def play(grid, T):
    for t in range(1, T + 1):
        neigh_counts = defaultdict(int)

        # make copy while getting rid of white tiles (False) from data structure
        grid = defaultdict(bool, {k: v for k, v in grid.items() if v})
        new_grid = deepcopy(grid)

        for pos in grid:
            for n in neighbors(pos):
                neigh_counts[n] += 1

        for pos, value in grid.items():
            if value is True and pos not in neigh_counts:  # black tile with 0 neighbors
                new_grid[pos] = False

        for pos, count in neigh_counts.items():
            if grid[pos] is True and count > 2:  # black
                new_grid[pos] = False
            elif grid[pos] is False and count == 2:
                new_grid[pos] = True
            else:
                pass  # tile stays the same

        grid = new_grid
    return sum(grid.values())


with open('input/24-1-test.txt') as f:
    test_positions = [sum(parse(line)) for line in f.read().splitlines()]
starting_floor = flip(test_positions)
assert play(starting_floor, 100) == 2208

positions = [sum(parse(line)) for line in get_input(day=24)]
starting_floor = flip(positions)
print(play(starting_floor, 100))
