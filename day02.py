from dataclasses import dataclass
import re

from aoc import get_input


@dataclass
class Entry:
    letter: str
    pol_min: int
    pol_max: int
    password: str


database = []
for line in get_input(day=2):
    pol_min, pol_max, letter, pw = re.fullmatch(r'(\d+)-(\d+) (\w): (\w+)', line).groups()
    database.append(Entry(letter, int(pol_min), int(pol_max), pw))

# 2-1
print(sum(entry.pol_min <= entry.password.count(entry.letter) <= entry.pol_max
          for entry in database))

# 2-2
n_valid = 0
for entry in database:
    first = entry.password[entry.pol_min - 1] == entry.letter
    second = entry.password[entry.pol_max - 1] == entry.letter

    if first ^ second:  # xor
        n_valid += 1
print(n_valid)

