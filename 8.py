from collections import defaultdict, Counter, deque
from dataclasses import dataclass
import heapq
from itertools import combinations, combinations_with_replacement, permutations, product
import re

import copy

from aoc import get_input

instructions = get_input(day=8)


# 8-1
i = 0
acc = 0
executed = set()
while i not in executed:
    executed.add(i)

    op, value = instructions[i].split()
    value = int(value)

    if op == 'nop':
        i += 1
    elif op == 'acc':
        acc += value
        i += 1
    elif op == 'jmp':
        i += value
    else:
        raise ValueError

print(acc)


# 8-2
def perturbed_instructions(original):
    original = [line.split() for line in original]

    for i, line in enumerate(original):
        if line[0] == 'nop':
            new = copy.deepcopy(original)
            new[i][0] = 'jmp'
            yield new
        elif line[0] == 'jmp':
            new = copy.deepcopy(original)
            new[i][0] = 'nop'
            yield new

this_one_right_here_officer = False
original = instructions
for instructions in perturbed_instructions(original):
    i = 0
    acc = 0
    executed = set()
    while i not in executed and 0 <= i < len(instructions):
        executed.add(i)

        op, value = instructions[i]
        value = int(value)

        if op == 'nop':
            i += 1
        elif op == 'acc':
            acc += value
            i += 1
        elif op == 'jmp':
            i += value
        else:
            raise ValueError

    if i == len(instructions):
        this_one_right_here_officer = True
        break

if this_one_right_here_officer:
    print(acc)



