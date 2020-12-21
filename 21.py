from collections import defaultdict, Counter, deque
from copy import deepcopy
from dataclasses import dataclass
from functools import cache
import heapq
from itertools import combinations, combinations_with_replacement, groupby, permutations, product, starmap, takewhile
from pprint import pprint
import re

import networkx as nx
from networkx.algorithms.bipartite.matching import maximum_matching

from aoc import get_input


class CounterFactualError(ValueError):
    pass


def parse(input_):
    ing_lines, aller_lines = [], []
    for product in input_:
        ingredients_str, allergens_str = product.split(' (contains ')

        ing_lines.append(list(ingredients_str.split(' ')))

        aller = [a.strip() for a in allergens_str[:-1].split(',')]
        aller_lines.append(aller)

    all_ingredients = set(i for ing in ing_lines for i in ing)
    all_allergens = set(a for aller in aller_lines for a in aller)

    ingredients = defaultdict(lambda: deepcopy(all_ingredients))
    # allergens = defaultdict(lambda: set(a for aller in aller_lines for a in aller))

    for ing_line, aller_line in zip(ing_lines, aller_lines):
        for aller in aller_line:
            ingredients[aller] &= set(ing_line)


    solution = {}
    while any(len(possibilities) >= 1 for possibilities in ingredients.values()):
        min_aller, min_ings = min(ingredients.items(), key=lambda x: len(x[1]))

        if len(min_ings) == 1:
            min_ing = list(min_ings)[0]
            solution[min_aller] = min_ing
            for aller in ingredients:
                ingredients[aller].discard(min_ing)
            del ingredients[min_aller]
        else:
            raise ValueError

    no_allergens = all_ingredients - set(solution.values())
    answer = 0
    for ing_line in ing_lines:
        for no_allergen in no_allergens:
            answer += ing_line.count(no_allergen)
    return solution, answer

# 21-1 test
with open('input/21-1-test.txt') as f:
    _, answer = parse(f.read().splitlines())
    assert answer == 5

# 21-1
solution, answer = parse(get_input(day=21))
print(answer)

# 21-2
print(','.join(solution[allergen] for allergen in sorted(solution)))
