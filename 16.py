import math
import re

from aoc import get_input

ipt = get_input(day=16)

rules = {}
for line in ipt[:20]:
    name, l1, u1, l2, u2 = re.fullmatch(r'([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)', line).groups()
    l1, u1, l2, u2 = map(int, (l1, u1, l2, u2))
    rules[name] = range(l1, u1+1), range(l2, u2+1)

your_ticket = [int(n) for n in ipt[22].split(',')]
nearby_tickets = [tuple(map(int, line.split(','))) for line in ipt[25:]]
N = len(your_ticket)


# 16-1
error_rate = 0
invalid_tickets = set()
for ticket in nearby_tickets:
    for num in ticket:
        is_valid = False
        for range1, range2 in rules.values():
            if num in range1 or num in range2:
                is_valid = True
                break
        if not is_valid:
            error_rate += num
            invalid_tickets |= {ticket}
valid_tickets = set(nearby_tickets) - invalid_tickets
print(error_rate)

# 16-2
rules_posses = {}
for rule, (r1, r2) in rules.items():
    valid_posses = set(range(N))
    for pos in range(N):
        for ticket in valid_tickets:
            num = ticket[pos]
            if not (int(num) in r1 or int(num) in r2):
                valid_posses -= {pos}
    rules_posses[rule] = valid_posses

unfixed_posses = rules_posses
final_posses = {}
while unfixed_posses:
    shortest_rule, shortest_pos = [(k, v) for k, v in sorted(unfixed_posses.items(), key=lambda item: len(item[1]))][0]
    assert len(shortest_pos) == 1

    final_posses[shortest_rule] = list(shortest_pos)[0]
    unfixed_posses = {rule: posses - shortest_pos for rule, posses in unfixed_posses.items() if rule != shortest_rule}

print(math.prod(your_ticket[pos] for rule, pos in final_posses.items() if rule.startswith('departure')))
