def decrease(cup, by, max_value):
    """decrease by one, wrap around from 1, not 0"""
    return (cup - by - 1) % max_value + 1


def linked_list(cups):
    next_ = [None] * (len(cups) + 1)  # mimic one-based-indexing by leaving index zero empty

    for i in range(len(cups) - 1):
        next_[cups[i]] = cups[i+1]
    next_[cups[-1]] = cups[0]

    return next_


def play(next_, start_cup, moves):
    max_value = len(next_) - 1

    current_cup = start_cup
    for move in range(1, moves + 1):
        c1 = next_[current_cup]
        c2 = next_[c1]
        c3 = next_[c2]

        destination_cup = decrease(current_cup, 1, max_value)
        while destination_cup in (c1, c2, c3):
            destination_cup = decrease(destination_cup, 1, max_value)

        next_[current_cup] = next_[c3]
        next_[destination_cup], next_[c3] = c1, next_[destination_cup]

        current_cup = next_[current_cup]

    return next_


def linked_list_to_sequence(next_, start_at=1, max_len=None):
    end = max_len - 1 if max_len is not None else len(next_) - 2

    cups = [start_at]
    prev = start_at
    for _ in range(end):
        prev = next_[prev]
        cups.append(prev)
    return cups


# 23-1
test = [int(c) for c in '389125467']
clockwise = [int(c) for c in '643719258']

assert linked_list([int(c) for c in '389125467']) == [None, 2, 5, 8, 6, 4, 7, 3, 9, 1]
assert linked_list_to_sequence(play(linked_list(test), start_cup=test[0], moves=10), start_at=8) == [int(c) for c in '837419265']
assert linked_list_to_sequence(play(linked_list(test), start_cup=test[0], moves=100), start_at=1)[1:] == [int(c) for c in '67384529']

print(''.join(str(c) for c in linked_list_to_sequence(
    play(linked_list(clockwise), start_cup=clockwise[0], moves=100),
    start_at=1)[1:]))

# 23-2
clockwise = [int(c) for c in '643719258'] + list(range(10, 1_000_000 + 1))

result = play(linked_list(clockwise), start_cup=clockwise[0], moves=10_000_000)

_, c1, c2 = linked_list_to_sequence(result, start_at=1, max_len=3)
print(f'{c1=}, {c2=}, {c1 * c2}')
