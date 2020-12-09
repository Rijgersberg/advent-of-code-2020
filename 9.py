from collections import defaultdict, Counter, deque
from dataclasses import dataclass
import heapq
from itertools import combinations, combinations_with_replacement, permutations, product
import re

from aoc import get_input

code = [int(line) for line in get_input(day=9)]

# 9-1
N = 25
i = N
for i in range(N, len(code)):
    if not code[i] in {sum(c) for c in combinations(code[i-N:i], 2)}:
        target = code[i]
        print(target)
        break

# 9-2
for i in range(len(code)):
    j = i + 1
    running_total = code[i]
    while j < len(code) and running_total < target:
        running_total += code[j]
        if running_total == target:
            print(i, j, min(code[i:j+1]) + max(code[i:j+1]))
            break
        j += 1
