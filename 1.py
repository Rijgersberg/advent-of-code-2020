from itertools import combinations

from aoc import fetch_input

expenses = [int(l) for l in fetch_input(day=1)]

# 1-1
for e1, e2 in combinations(expenses, 2):
    if e1 + e2 == 2020:
        print(e1, e2, e1 * e2)

# 1-2
for e1, e2, e3 in combinations(expenses, 3):
    if e1 + e2 + e3 == 2020:
        print(e1, e2, e3, e1 * e2 * e3)
