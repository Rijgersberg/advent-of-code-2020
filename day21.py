from collections import defaultdict
from copy import deepcopy

from aoc import get_input


def parse(input_):
    ing_lines, aller_lines = [], []
    for product in input_:
        ingredients_str, allergens_str = product.split(' (contains ')

        ing_lines.append(list(ingredients_str.split(' ')))

        aller = [a.strip() for a in allergens_str[:-1].split(',')]
        aller_lines.append(aller)

    all_ingredients = set(i for ing in ing_lines for i in ing)
    return ing_lines, aller_lines, all_ingredients


def get_constraints(ing_lines, aller_lines, all_ingredients):
    ingredients = defaultdict(lambda: deepcopy(all_ingredients))
    for ing_line, aller_line in zip(ing_lines, aller_lines):
        for aller in aller_line:
            ingredients[aller] &= set(ing_line)
    return ingredients


def solve(ingredients):
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
    return solution


def do(input_):
    ing_lines, aller_lines, all_ingredients = parse(input_)
    constraints = get_constraints(ing_lines, aller_lines, all_ingredients)
    solution = solve(constraints)

    no_allergens = all_ingredients - set(solution.values())
    answer = 0
    for ing_line in ing_lines:
        for no_allergen in no_allergens:
            answer += ing_line.count(no_allergen)
    return solution, answer


# 21-1 test
with open('input/21-1-test.txt') as f:
    _, answer = do(f.read().splitlines())
    assert answer == 5

# 21-1
solution, answer = do(get_input(day=21))
print(answer)

# 21-2
print(','.join(solution[allergen] for allergen in sorted(solution)))
