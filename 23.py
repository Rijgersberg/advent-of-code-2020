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

        # print(f'{move=}, {destination_cup=}, {list(cups)[:100]}, {list(cups)[-100:]}')

    return list(cups)

def reorder(cups, start_at=1):
    start_idx = cups.index(start_at)

    return [start_at] + cups[start_idx + 1:] + cups[:start_idx]


def linked_list(cups):
    print(f'len of cups is {len(cups)}')
    next_ = [None] * (len(cups) + 1)  # mimic one-based-indexing
    print(f'len of next_ is {len(next_)}')
    for i in range(len(cups) - 1):
        next_[cups[i]] = cups[i+1]
    next_[cups[-1]] = cups[0]

    return next_

def play2(next_, start_cup, moves):
    max_value = len(next_) - 1

    current_cup = start_cup
    for move in range(1, moves + 1):
        c1 = next_[current_cup]
        c2 = next_[c1]
        c3 = next_[c2]

        destination_cup = decrease(current_cup, 1, max_value)
        while destination_cup in (c1, c2, c3):
            destination_cup = decrease(destination_cup, 1, max_value)

        next_[current_cup] = next_[c3]

        old_right_of_dest = next_[destination_cup]
        next_[destination_cup] = c1
        # next of c1 and c2 stay the same
        next_[c3] = old_right_of_dest

        current_cup = next_[current_cup]

    return next_

def linked_list_to_sequence(next_, start_at=1):
    cups = [start_at]
    prev = start_at
    for i in range(len(next_) - 2):
        if prev >= len(next_):
            print(i, prev, len(next_))
        prev = next_[prev]
        cups.append(prev)
    return cups


# 23-1
test = [int(c) for c in '389125467']
clockwize = [int(c) for c in '643719258']

assert linked_list([int(c) for c in '389125467']) == [None, 2, 5, 8, 6, 4, 7, 3, 9, 1]
assert linked_list_to_sequence(play2(linked_list(deepcopy(test)), start_cup=test[0], moves=10), start_at=8) == [int(c) for c in '837419265']
assert linked_list_to_sequence(play2(linked_list(deepcopy(test)), start_cup=test[0], moves=100), start_at=1)[1:] == [int(c) for c in '67384529']

print(''.join(str(c) for c in linked_list_to_sequence(play2(linked_list(deepcopy(clockwize)), start_cup=clockwize[0], moves=100), start_at=1)[1:]))

# 23-2
print('=' * 80)

clockwize = [int(c) for c in '643719258'] + list(range(10, 1_000_000+1))

t0 = time.time()
moves = 10_000_000
input_2 = linked_list(deepcopy(clockwize))
print(f'len of input_2 is {len(input_2)}')
result = play2(input_2, start_cup=clockwize[0], moves=moves)
print(f'len of results is {len(result)}')
t = time.time() - t0
print(f'{t} seconds, {moves / t} per second, {t/moves * 10_000_000 / 60} minutes for 10 million moves')
c1, c2 = linked_list_to_sequence(result, start_at=1)[1:3]

print(f'{c1=}, {c2=}, {c1 * c2}')