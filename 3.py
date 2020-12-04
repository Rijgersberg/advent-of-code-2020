import math

from aoc import get_input

forest = get_input(day=3)

# 3-1
dx = 3
dy = 1

N = 0
for y, row in enumerate(forest):
    current_pos = row[y * dx % len(row)]

    if current_pos == '#':
        N += 1
print(N)

# 3-2
N_trees = []
for dx, dy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    N_trees.append(0)
    for n, y in enumerate(range(0, len(forest), dy)):
        row = forest[y]
        current_pos = row[n * dx % len(row)]

        if current_pos == '#':
            N_trees[-1] += 1

print(math.prod(N_trees))


# 3-2 oneliner
print(
    math.prod(
        sum(row[n * dx % len(row)] == '#'
            for n, row in enumerate(forest[::dy]))
        for dx, dy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    )
)
