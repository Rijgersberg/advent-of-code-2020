from itertools import product, count
import re

from aoc import get_input

instructions = get_input(day=14)


# 14-1
mask = {}
mem = {}
for instruction in instructions:
    if instruction.startswith('mask'):
        _, mask = instruction.split(' = ')
    else:
        index, value = re.fullmatch(r'mem\[(\d+)\] = (\d+)', instruction).groups()

        mem[int(index)] = int(''.join(
            c if mask[i] == 'X' else mask[i]
            for i, c in enumerate(f'{int(value):036b}')),
            2)
print(sum(mem.values()))

# 14-2
mem = {}
for instruction in instructions:
    if instruction.startswith('mask'):
        _, mask = instruction.split(' = ')
    else:
        index, value = re.fullmatch(r'mem\[(\d+)\] = (\d+)', instruction).groups()

        for filler in product(('0', '1'), repeat=mask.count('X')):
            counter = count()
            med_idx = int(''.join(
                mask[i] if mask[i] == '1' else filler[next(counter)] if mask[i] == 'X' else c
                for i, c in enumerate(f'{int(index):036b}')),
                2)
            mem[med_idx] = int(value)
print(sum(mem.values()))
