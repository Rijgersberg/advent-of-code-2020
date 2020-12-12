from aoc import get_input

# Argh, this here ships sails the complex plane
instructions = [(i[0], int(i[1:])) for i in get_input(day=12)]

def move1(pos, direction, action, value):
    if action == 'N':
        pos += 1j * value
    elif action == 'S':
        pos += -1j * value
    elif action == 'E':
        pos += 1 * value
    elif action == 'W':
        pos += -1 * value
    elif action == 'L':
        for n in range(value // 90):
            direction = (direction - 1) % 4
    elif action == 'R':
        for n in range(value // 90):
            direction = (direction + 1) % 4
    elif action == 'F':
        pos += value * (1j, 1, -1j, -1)[direction]
    else:
        raise ValueError
    return pos, direction


def move2(pos, wp, action, value):
    if action == 'N':
        wp += 1j * value
    elif action == 'S':
        wp += -1j * value
    elif action == 'E':
        wp += 1 * value
    elif action == 'W':
        wp += -1 * value
    elif action == 'L':
        for n in range(value // 90):
            wp *= 1j
    elif action == 'R':
        for n in range(value // 90):
            wp *= -1j
    elif action == 'F':
        pos += value * wp
    else:
        raise ValueError
    return pos, wp

# 12-1
pos = 0
direction = 1
for action, value in instructions:
    pos, direction = move1(pos, direction, action, value)
print(abs(pos.real) + abs(pos.imag))

# 12-2
pos = 0
wp = 10 + 1j
for action, value in instructions:
    pos, wp = move2(pos, wp, action, value)
print(abs(pos.real) + abs(pos.imag))
