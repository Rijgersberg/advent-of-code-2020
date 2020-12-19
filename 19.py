import re

from aoc import get_input


def parse_input(input_str):
    rules_str, messages_str = input_str.split('\n\n')

    rules = {line.split(':')[0]: line.split(':')[1].strip() for line in rules_str.splitlines()}
    messages = messages_str.splitlines()
    return rules, messages


def pattern(n):
    rule = rules[n]

    if PART == 2:
        if n == '8':
            return f"({pattern('42')})+"
        elif n == '11':
            # 42 31 | 42 42 31 31 | 42 42 42 31 31 31 | ...
            enough = 10  # wow...
            return '(' + '|'.join(f"{pattern('42')}{{{i}}}{pattern('31')}{{{i}}}" for i in range(1, enough)) + ')'

    if '"a"' in rule:
        return 'a'
    elif '"b"' in rule:
        return 'b'
    elif '|' in rule:
        p1, p2 = rule.split('|')
        p1, p2 = p1.strip(), p2.strip()
        return f'({"".join(map(pattern, p1.split(" ")))}|{"".join(map(pattern, p2.split(" ")))})'
    else:
        return ''.join(map(pattern, rule.split(' ')))


# test-1
PART = 1
with open('input/19-1-test.txt') as f:
    rules, messages = parse_input(f.read())
assert sum(re.fullmatch(pattern('0'), message) is not None for message in messages) == 2

# test-2
PART = 2
with open('input/19-2-test.txt') as f:
    rules, messages = parse_input(f.read())
assert sum(re.fullmatch(pattern('0'), message) is not None for message in messages) == 12

# 19
rules, messages = parse_input(get_input(day=19, as_list=False))

# 19-1
PART = 1
print(sum(re.fullmatch(pattern('0'), message) is not None for message in messages))

# 19-2
PART = 2
print(sum(re.fullmatch(pattern('0'), message) is not None for message in messages))
