from collections import defaultdict, Counter, deque
from dataclasses import dataclass
import heapq
from itertools import combinations, combinations_with_replacement, permutations, product
import re

from aoc import get_input

groups = '\n'.join(get_input(day=6)).split('\n\n')


# 6-1
total = 0
for group in groups:
    yesses = set()
    for person in group.split('\n'):
        yesses.update(person)

    total += len(yesses)

print(total)

# 6-2
total = 0
for group in groups:
    yesses = Counter()

    persons = group.split('\n')
    for person in persons:
        yesses.update(Counter(person))

    n_yesses = sum(yesses[c] == len(persons) for c in yesses)

    total += n_yesses

print(total)