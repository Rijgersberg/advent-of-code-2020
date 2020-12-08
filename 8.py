import copy

from aoc import get_input

instructions = get_input(day=8)


def parse(instructions):
    parsed = []
    for instruction in instructions:
        op, value = instruction.split()
        parsed.append([op, int(value)])
    return parsed


def run(instructions):
    i = 0
    acc = 0
    executed = set()
    while i not in executed and 0 <= i < len(instructions):
        executed.add(i)

        op, value = instructions[i]

        if op == 'nop':
            i += 1
        elif op == 'acc':
            acc += value
            i += 1
        elif op == 'jmp':
            i += value
        else:
            raise ValueError

    return i, acc


# 8-1
i, acc = run(parse(instructions))
print(acc)


# 8-2
def perturbed_instructions(original):
    for i, line in enumerate(original):
        if line[0] == 'nop':
            new = copy.deepcopy(original)
            new[i][0] = 'jmp'
            yield new
        elif line[0] == 'jmp':
            new = copy.deepcopy(original)
            new[i][0] = 'nop'
            yield new


for instructions in perturbed_instructions(parse(instructions)):
    i, acc = run(instructions)

    if i == len(instructions):
        print(acc)
        break
