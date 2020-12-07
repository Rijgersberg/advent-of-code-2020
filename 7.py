from collections import defaultdict
import re

from aoc import get_input

rules = get_input(day=7)


def clean(bagstring):
    number, modifier, color, bag = re.fullmatch(r'(\d+) ([a-z]+) ([a-z]+) (bag)s?', bagstring).groups()
    return int(number), ' '.join((modifier, color))

fits_in = defaultdict(set)
holds = defaultdict(set)

for rule in rules:
    outer, inners = rule.split(' contain ')
    outer = outer[:-5]

    for inner in inners.split(','):
        inner = inner.strip()
        if inner[-1] == '.':
            inner = inner[:-1]

        if inner != 'no other bags':
            number, kind = clean(inner)

            fits_in[kind].add((number, outer))
            holds[outer].add((number, kind))
print(fits_in)
print(holds)


# 7-1
def can_contain(color):
    if color not in fits_in:
        return {}
    else:
        x = fits_in[color]
        return set.union({v[1] for v in x}, *[can_contain(c) for n, c in fits_in[color]])

print(len(can_contain('shiny gold')))


# 7-2
def n_required(color):
    if color not in holds:
        return 1
    else:
        return 1 + sum(n * n_required(c) for n, c in holds[color])

print(n_required('shiny gold') - 1)
