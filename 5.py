from collections import defaultdict, Counter, deque
from dataclasses import dataclass
import heapq
from itertools import combinations, combinations_with_replacement, permutations, product
import re

from aoc import get_input

seat_strings = (get_input(day=5))

# 5-1
mapping = {'F': '0', 'B': '1',
           'L': '0', 'R': '1'}


def seatid(seat_string):
    binstring = ''.join(mapping[c] for c in seat_string)
    return int(binstring, 2)


assert seatid('FBFBBFFRLR') == 357
assert seatid('BFFFBBFRRR') == 567
assert seatid('FFFBBBFRRR') == 119
assert seatid('BBFFBBFRLL') == 820

seats = {seatid(s) for s in seat_strings}
print(max(seats))

# 5-2
for s in range(max(seats)):
    if s not in seats and s - 1 in seats and s + 1 in seats:
        print(s)
