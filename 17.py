from collections import defaultdict

from aoc import get_input


def neighbors(x, y, z):
    for i in (x-1, x, x+1):
        for j in (y-1, y, y+1):
            for k in (z-1, z, z+1):
                if (i, j, k) != (x, y, z):
                    yield i, j, k


def update(grid):
    counts = defaultdict(int)
    for x, y, z in grid:
        for xn, yn, zn in neighbors(x, y, z):
            counts[(xn, yn, zn)] += 1

    return {pos for pos, count in counts.items()
            if (pos in grid and 2 <= count <= 3)
            or (pos not in grid and count == 3)}


# 17-1
grid = set()
for y, line in enumerate(get_input(day=17)):
    for x, c in enumerate(line):
        if c == '#':
            grid.add((x, y, 0))

for t in range(1, 6 + 1):
    grid = update(grid)
print(len(grid))


# 17-2
def neighbors2(x, y, z, w):
    for i in (x-1, x, x+1):
        for j in (y-1, y, y+1):
            for k in (z-1, z, z+1):
                for m in (w-1, w, w+1):
                    if (i, j, k, m) != (x, y, z, w):
                        yield i, j, k, m

def update2(grid):
    counts = defaultdict(int)
    for x, y, z, w in grid:
        for xn, yn, zn, wn in neighbors2(x, y, z, w):
            counts[(xn, yn, zn, wn)] += 1

    return {pos for pos, count in counts.items()
            if (pos in grid and 2 <= count <= 3)
            or (pos not in grid and count == 3)}


grid = set()
for y, line in enumerate(get_input(day=17)):
    for x, c in enumerate(line):
        if c == '#':
            grid.add((x, y, 0, 0))

for t in range(1, 6 + 1):
    grid = update2(grid)
print(len(grid))
