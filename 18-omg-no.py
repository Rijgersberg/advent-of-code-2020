from enum import Enum, auto

from aoc import get_input

equations = get_input(day=18)


class Operator(Enum):
    PLUS = auto()
    MULT = auto()

def find_close(string):
    # print(f'calling find_close on "{string}"')
    level = 0

    for i, c in enumerate(string):
        if c == '(':
            level += 1
        elif c == ')':
            level -= 1
        if level == 0:
            return i
    else:
        raise Exception


def parse(equation):
    ans = 0
    op = Operator.PLUS

    pos = 0
    # print(f'parsing "{equation}"')
    while pos < len(equation):
        c = equation[pos]
        # print(f'{pos=}, c="{c}"')

        if c == '(':
            close = pos + find_close(equation[pos:])
            c = str(parse(equation[pos+1:close]))
            pos = close
        elif c == ')':
            raise ValueError

        if c.isnumeric():
            c = int(c)
            if op == Operator.PLUS:
                ans += c
                op = None
            elif op == Operator.MULT:
                ans *= c
                op = None
            else:
                raise ValueError(f'Encountered a number {c=} at {pos=} without having a value operator set')
        elif c == '+':
            op = Operator.PLUS
        elif c == '*':
            op = Operator.MULT
        elif c == ' ':
            pass
        else:
            raise ValueError
        pos += 1

    return ans


# 18-1
print(sum(parse(equation) for equation in equations))


# 18-2
def find_end_of_addition(string):
    i = 0
    while i < len(string):
        c = string[i]
        if c == '(':
            i += find_close(string[i:])
        elif c in ')+':
            return i
        i += 1
    return i


def add_parens(equation):
    print('')
    print(equation)
    pos = 0
    while pos < len(equation):
        c = equation[pos]

        if c == '+':
            close = find_end_of_addition(equation[pos+1:])  # TODO ook in de haakjes die je tegenkomt moet add_parens draaien
            print()
            print(equation)
            todo_part = f'TODO:[{equation[pos+1:pos+close-2]}]'
            equation = equation[:pos+1] + '(' + todo_part + ')' + equation[pos+close-2:]
            pos +=
            print(equation)
        pos += 1  # TODO je moet wel over alles heen skippen
    print(equation)
    return equation


print(sum(parse(add_parens(equation)) for equation in equations))