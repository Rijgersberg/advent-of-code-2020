from collections import deque

from aoc import get_input


def parse(input_):
    deck1 = deque()
    deck2 = deque()
    for line in input_:
        if line == 'Player 1:':
            deck = deck1
        elif line == 'Player 2:':
            deck = deck2
        elif line.isnumeric():
            deck.append(int(line))
    return deck1, deck2


def play(deck1, deck2):
    round = 0
    while deck1 and deck2:
        round += 1
        c1, c2 = deck1.popleft(), deck2.popleft()

        if c1 > c2:
            deck1.append(c1)
            deck1.append(c2)
        elif c2 > c1:
            deck2.append(c2)
            deck2.append(c1)
        else:
            raise ValueError
    return deck1 if deck1 else deck2


def score(deck):
    return sum(i * c for i, c in enumerate(reversed(deck), 1))


# 22-1 test
with open('input/22-1-test.txt') as f:
    assert score(play(*parse(f.read().splitlines()))) == 306

# 22-1
print(score(play(*parse(get_input(day=22)))))


# 22-2
def freeze(deck1, deck2):
    return tuple(deck1), tuple(deck2)


def play_recursive(deck1, deck2):
    round = 0
    seen = set()
    while deck1 and deck2:
        round += 1

        frozen_decks = freeze(deck1, deck2)
        if frozen_decks in seen:
            return 1, frozen_decks
        else:
            seen.add(frozen_decks)

        c1, c2 = deck1.popleft(), deck2.popleft()

        if len(deck1) >= c1 and len(deck2) >= c2:
            # To play a sub-game of Recursive Combat, each player creates a new deck by making a copy of the next cards
            # in their deck (the quantity of cards copied is equal to the number on the card they drew to trigger the sub-game).
            new_deck_1 = deque(list(deck1)[:c1])
            new_deck_2 = deque(list(deck2)[:c2])
            winner, _ = play_recursive(new_deck_1, new_deck_2)
        else:
            winner = 1 if c1 > c2 else 2

        if winner == 1:
            deck1.append(c1)
            deck1.append(c2)
        elif winner == 2:
            deck2.append(c2)
            deck2.append(c1)
        else:
            raise ValueError
    return 1 if deck1 else 2, deck1 if deck1 else deck2


# 22-2 test
with open('input/22-1-test.txt') as f:
    assert score(play_recursive(*parse(f.read().splitlines()))[1]) == 291

# 22-2
print(score(play_recursive(*parse(get_input(day=22)))[1]))
