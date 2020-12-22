from aoc import get_input


def parse(input_):
    p1_str, p2_str = input_.split('\n\n')
    return tuple(int(l) for l in p1_str.splitlines()[1:]), \
           tuple(int(l) for l in p2_str.splitlines()[1:])


def play(deck1, deck2, recursive=False):
    seen = set()
    while deck1 and deck2:
        if recursive:
            if (deck1, deck2) in seen:
                return 1, (deck1, deck2)
            else:
                seen.add((deck1, deck2))

        c1, deck1 = deck1[0], deck1[1:]
        c2, deck2 = deck2[0], deck2[1:]

        if recursive and len(deck1) >= c1 and len(deck2) >= c2:
            winner, _ = play(deck1[:c1], deck2[:c2], recursive)
        else:
            winner = 1 if c1 > c2 else 2

        if winner == 1:
            deck1 = (*deck1, c1, c2)
        elif winner == 2:
            deck2 = (*deck2, c2, c1)

    return 1 if deck1 else 2, deck1 if deck1 else deck2


def score(deck):
    return sum(i * c for i, c in enumerate(reversed(deck), 1))


# 22-1
print(score(play(*parse(get_input(day=22, as_list=False)))[1]))

# 22-2
print(score(play(*parse(get_input(day=22, as_list=False)), recursive=True)[1]))
