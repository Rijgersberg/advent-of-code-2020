from aoc import get_input


def find_close(string):
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
    equation = equation.replace(' ', '')
    ans = 0
    op = '+'

    pos = 0
    while pos < len(equation):
        c = equation[pos]

        if c == '(':
            close = pos + find_close(equation[pos:])
            c = str(parse(equation[pos+1:close]))  # recursion
            pos = close
        elif c == ')':
            raise ValueError

        if c.isnumeric():
            if op == '+':
                ans += int(c)
                op = None
            elif op == '*':
                ans *= int(c)
                op = None
            else:
                raise ValueError(f'Encountered a number {c=} at {pos=} without having an operator set')
        elif c in '+*':
            op = c
        else:
            raise ValueError(c)
        pos += 1

    return ans


# 18-1
equations = get_input(day=18)
print(sum(parse(equation) for equation in equations))
