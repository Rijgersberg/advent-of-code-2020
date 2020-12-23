from collections import defaultdict, Counter, deque
from copy import deepcopy
from dataclasses import dataclass
from functools import cache
import heapq
from itertools import combinations, combinations_with_replacement, groupby, permutations, product, starmap, takewhile
import re
import time

from aoc import get_input

def decrease(cup, by, max_value):
    '''decrease by one wrap around from 1, not 0'''
    return (cup - by - 1) % max_value + 1


def play(cups, moves):
    max_value = max(cups)

    for move in range(1, moves+1):
        # print()
        # print(f'-- {move=} -- ')
        # print(f'{cups=}')
        current_cup = cups.popleft()
        c1 = cups.popleft()
        c2 = cups.popleft()
        c3 = cups.popleft()
        # print(f'{current_cup}')
        # print(f'pick up: {c1}, {c2}, {c3}')

        destination_cup = decrease(current_cup, 1, max_value)
        while destination_cup in (c1, c2, c3):
            destination_cup = decrease(destination_cup, 1, max_value)

        dest_idx = cups.index(destination_cup)
        cups = deque([current_cup] + list(cups)[:dest_idx + 1] + [c1, c2, c3] + list(cups)[dest_idx + 1:])

        last = cups.popleft()
        cups.append(last)

        print(f'{move=}, {destination_cup=}, {list(cups)[:100]}, {list(cups)[-100:]}')

    return list(cups)

def reorder(cups, start_at=1):
    start_idx = cups.index(start_at)

    return [start_at] + cups[start_idx + 1:] + cups[:start_idx]


# 23-1
test = deque([int(c) for c in '389125467'])
clockwize = deque([int(c) for c in '643719258'])

assert play(deepcopy(test), 10) == [int(c) for c in '837419265']
assert reorder(play(deepcopy(test), 100))[1:] == [int(c) for c in '67384529']

print(''.join(str(c) for c in reorder(play(clockwize, 100))[1:]))

# 23-2
print('=' * 80)
clockwize = deque([int(c) for c in '643719258'] + list(range(10, 1_000_000+1)))

t0 = time.time()
moves = 100
result = play(clockwize, moves)
t = time.time() - t0
print(f'{t} seconds, {moves / t} per second, {moves / t * 10_000_000 / 60 / 60 / 24} days for 10 million moves')

