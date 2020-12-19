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
            return '(' + pattern('42') + ')+'
        elif n == '11':
            # 42 31 | 42 42 31 31 | 42 42 42 31 31 31 | ...
            enough = 6  # wow
            return '(' + '|'.join(f"{pattern('42')}{{{i}}}{pattern('31')}{{{i}}}" for i in range(1, enough)) + ')'

    if '"a"' in rule:
        return 'a'
    elif '"b"' in rule:
        return 'b'
    elif '|' in rule:
        p1, p2 = rule.split(' | ')
        return '(' + ''.join(pattern(c) for c in p1.split(' ')) + '|' + ''.join(pattern(c) for c in p2.split(' ')) + ')'
    else:
        return ''.join(pattern(c) for c in rule.split(' '))


def n_valid(messages, start):
    c_pattern = re.compile(pattern(start))
    return sum(re.fullmatch(c_pattern, message) is not None for message in messages)


# test-1
PART = 1
with open('input/19-1-test.txt') as f:
    rules, messages = parse_input(f.read())
assert n_valid(messages, start='0') == 2

# test-2
PART = 2
with open('input/19-2-test.txt') as f:
    rules, messages = parse_input(f.read())
assert n_valid(messages, start='0') == 12

# 19
rules, messages = parse_input(get_input(day=19, as_list=False))

# 19-1
PART = 1
print(n_valid(messages, start='0'))

# 19-2
PART = 2
print(n_valid(messages, start='0'))
