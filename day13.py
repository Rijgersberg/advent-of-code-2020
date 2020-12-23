from collections import defaultdict, Counter, deque
from dataclasses import dataclass
import heapq
from itertools import combinations, combinations_with_replacement, permutations, product
import re

from aoc import get_input

inpt = get_input(day=13)
eta = int(inpt[0])
schedule = inpt[1].split(',')

# 13-1
min_wait = float('inf')
min_bus = None
for bus in schedule:
    if not bus == 'x':
        bus = int(bus)
        wait = bus - (eta % bus)
        if wait < min_wait:
            min_wait = wait
            min_bus = bus

print(min_bus, min_wait, min_bus * min_wait)

# schedule = '7,13,x,x,59,x,31,19'.split(',')
# schedule = '17,x,13,19'.split(',')
# schedule = '9,x,x,15'.split(',')


# 13-2
def extended_gcd(a, b):
    """from https://math.stackexchange.com/questions/2218763/how-to-find-lcm-of-two-numbers-when-one-starts-with-an-offset

    Extended Greatest Common Divisor Algorithm

    Returns:
        gcd: The greatest common divisor of a and b.
        s, t: Coefficients such that s*a + t*b = gcd

    Reference:
        https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Pseudocode
    """
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient, remainder = divmod(old_r, r)
        old_r, r = r, remainder
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t


examples = [
    ('7,13,x,x,59,x,31,19', 1068781),
    ('17,x,13,19', 3417),
    ('67,7,59,61', 754018),
    ('67,x,7,59,61', 779210),
    ('67,7,x,59,61', 1261476),
    ('1789,37,47,1889', 1202161486),
]

def t_first(schedule):
    rules = []
    for dt, bus in enumerate(schedule):
        if not bus == 'x':
            rules.append((dt, int(bus)))
    print(rules)

    p_a = rules[0][1]
    phase_a = -rules[0][0]

    for i in range(1, len(rules)):
        p_b = rules[i][1]
        phase_b = -rules[i][0]

        g, s, t = extended_gcd(p_a, p_b)
        lcm = p_a * p_b // g

        z = (phase_a - phase_b) // g
        m = z * s
        n = -z * t

        phase_a = (-m * p_a + phase_a) % lcm
        p_a = lcm
    return lcm, phase_a


for example_schedule, answer in examples:
    freq, phase_a = t_first(example_schedule.split(','))

    assert phase_a == answer
    print(f'{freq=}, {phase_a=}, {answer=}')

freq, phase_a = t_first(schedule)
print(f'{freq=}, {phase_a=}')
