from collections import defaultdict, Counter, deque
from dataclasses import dataclass
import heapq
from itertools import combinations, combinations_with_replacement, permutations, product
import re
import string

from aoc import get_input

batchfile = '\n'.join(get_input(day=4)).split('\n\n')

# 4-1
required_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

passports = [{kv.split(':')[0]: kv.split(':')[1] for kv in entry.split()}
             for entry in batchfile]

print(sum(all(key in passport for key in required_fields)
          for passport in passports))

# 4-2
N_valid = 0
for passport in passports:
    try:
        assert(1920 <= int(passport.get('byr', 0)) <= 2002)
        assert(2010 <= int(passport.get('iyr', 0)) <= 2020)
        assert(2020 <= int(passport.get('eyr', 0)) <= 2030)

        # height
        height = passport.get('hgt', '')
        assert(height.endswith(('cm', 'in')))
        unit = height[-2:]
        measurement = height[:-2]
        assert(measurement.isnumeric())
        measurement = int(measurement)

        if unit == 'cm':
            assert(150 <= measurement <= 193)
        elif unit == 'in':
            assert(59 <= measurement <= 76)

        # hair color
        hair_color = passport.get('hcl', '')
        assert(hair_color.startswith('#') and len(hair_color) == 7 and all(c in string.hexdigits for c in hair_color[-6:]))

        eye_color = passport.get('ecl', '')
        assert(eye_color in ('amb blu brn gry grn hzl oth'.split()))

        passport_id = passport.get('pid', '')
        assert(len(passport_id) == 9)
        assert(passport_id.isnumeric())

        print({k: passport[k] for k in sorted(passport.keys()) if k != 'cid'})
        N_valid += 1
    except AssertionError:
        pass
print(N_valid)