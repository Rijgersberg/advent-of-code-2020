from aoc import get_input


def transform(subject, loop_size):
    value = 1
    for _ in range(loop_size):
        value = (value * subject) % 20201227
    return value


def crack_loop_size(pubkey, subject, N=100_000):
    value = 1
    for loop_size in range(1, N):
        value = (value * subject) % 20201227
        if value == pubkey:
            return loop_size
    else:
        raise ValueError()


# 25-1
test_card_pubkey, test_door_pubkey = 5764801, 17807724
assert crack_loop_size(test_card_pubkey, 7) == 8
assert crack_loop_size(test_door_pubkey, 7) == 11

assert transform(test_door_pubkey, crack_loop_size(test_card_pubkey, 7)) == 14897079

card_pubkey, door_pubkey = [int(x) for x in get_input(day=25)]
print(transform(door_pubkey, crack_loop_size(card_pubkey, 7, N=100_000_000)))
