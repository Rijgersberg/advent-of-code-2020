import re

from aoc import get_input


def parse_rules(rules_str):
    return {line.split(':')[0]: line.split(':')[1].strip() for line in rules_str.splitlines()}


def pattern(n):
    rule = rules[n]

    global PART
    if PART == 2:
        if n == '8':
            return f"({pattern('42')})+"
        elif n == '11':
            # 42 31 | 42 42 31 31 | 42 42 42 31 31 31 | ...
            enough = 20
            return '(' + '|'.join(f"{pattern('42')}{{{i}}}{pattern('31')}{{{i}}}" for i in range(1, enough)) + ')'

    if '"a"' in rule:
        return r'a'
    elif '"b"' in rule:
        return r'b'
    elif '|' in rule:
        p1, p2 = rule.split('|')
        p1, p2 = p1.strip(), p2.strip()
        return fr'({"".join(map(pattern, p1.split(" ")))}|{"".join(map(pattern, p2.split(" ")))})'
    else:
        return r''.join(map(pattern, rule.split(' ')))


# test-1
PART = 1
rules = parse_rules('''0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"''')

messages = '''ababbb
bababa
abbbab
aaabbb
aaaabbb'''.splitlines()

assert sum(re.fullmatch(pattern('0'), message) is not None for message in messages) == 2

#test-2
PART = 2
rules = parse_rules('''42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1''')

messages = '''abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba'''.splitlines()

assert sum(re.fullmatch(pattern('0'), message) is not None for message in messages) == 12

# 19
puzzle_rules, messages = '\n'.join(get_input(day=19)).split('\n\n')
rules = parse_rules(puzzle_rules)
messages = messages.splitlines()

# 19-1
PART = 1
print(sum(re.fullmatch(pattern('0'), message) is not None for message in messages))

# 19-2
PART = 2
print(sum(re.fullmatch(pattern('0'), message) is not None for message in messages))
