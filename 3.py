from collections import defaultdict, Counter, deque
from dataclasses import dataclass
from itertools import combinations, combinations_with_replacement, permutations
import re

from aoc import fetch_input


@dataclass
class Entry:
    letter: str
    pol_min: int
    pol_max: int
    password: str


data = [int(l) for l in fetch_input(day=3)]

data = []
for line in fetch_input(day=3):
    pol_min, pol_max, letter, pw = re.fullmatch(r'(\d+)-(\d+) (\w): (\w+)', line).groups()
    data.append(Entry(letter, int(pol_min), int(pol_max), pw))

# 3-1




# 3-2
