from collections import Counter

from aoc import get_input

groups = get_input(day=6, as_list=False).split('\n\n')

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
        yesses.update(person)

    n_yesses = sum(yesses[c] == len(persons) for c in yesses)

    total += n_yesses

print(total)