from collections import defaultdict, Counter, deque
from dataclasses import dataclass
import heapq
from itertools import combinations, combinations_with_replacement, permutations, product
import re

from aoc import get_input

instructions = get_input(day=14)


# 14-1
mask = {}
mem = {}
for instruction in instructions:
    if instruction.startswith('mask'):
        mask_str = re.fullmatch(r'mask = ([01X]+)', instruction).groups()[0]
    else:
        index, value = re.fullmatch(r'mem\[(\d+)\] = (\d+)', instruction).groups()

        bit_list = list("{0:b}".format(int(value)).zfill(36))
        for i, v in enumerate(mask_str):
            if v != 'X':
                bit_list[i] = v
        mem[int(index)] = int(''.join(bit_list), 2)
print(sum(mem.values()))

# 14-2
mem = {}
for instruction in instructions:
    if instruction.startswith('mask'):

        mask_str = re.fullmatch(r'mask = ([01X]+)', instruction).groups()[0]
        mask_idc = [m.start() for m in re.finditer(r'X', mask_str)]
    else:
        index, value = re.fullmatch(r'mem\[(\d+)\] = (\d+)', instruction).groups()

        bit_str = "{0:b}".format(int(index)).zfill(36)
        if len(mask_idc) <= 4:
            print()
            print(bit_str)
            print(mask_str)
        for filler in product(('0', '1'), repeat=len(mask_idc)):
            bit_list = list(bit_str)

            filler_idx = 0
            for i, v in enumerate(mask_str):
                if v == '1':
                    bit_list[i] = v
                elif v == 'X':
                    bit_list[i] = filler[filler_idx]
                    filler_idx += 1
            med_idx = int(''.join(bit_list), 2)
            if len(mask_idc) <= 4:
                print(''.join(bit_list))

            mem[med_idx] = int(value)
print(sum(mem.values()))