from dataclasses import dataclass

from aoc import get_input


@dataclass
class RecursiveCombat:
    deck1: tuple[int]
    deck2: tuple[int]
    winner: int = None

    @staticmethod
    def parse(input_):
        p1, p2 = input_.split('\n\n')
        deck1 = tuple(int(l) for l in p1.splitlines()[1:])
        deck2 = tuple(int(l) for l in p2.splitlines()[1:])
        return RecursiveCombat(deck1, deck2)

    def play(s, recursive=False):
        seen = set
        while s.deck1 and s.deck2:
            if recursive:
                if (s.deck1, s.deck2) in seen:
                    return 1
                else:
                    seen.add((s.deck1, s.deck2))

            card1, s.deck1 = s.deck1[0], s.deck1[1:]
            card2, s.deck2 = s.deck2[0], s.deck2[1:]

            if recursive and len(s.deck1) >= card1 and len(s.deck2) >= card2:
                winner = RecursiveCombat(s.deck1[:card1], s.deck2[:card2]).play(recursive)
            else:
                winner = 1 if card1 > card2 else 2

            if winner == 1:
                s.deck1 += (card1, card2)
            elif winner == 2:
                s.deck2 += (card2, card1)

        s.winner = winner
        return winner

    @property
    def score(self):
        winning_deck = self.deck1 if self.winner == 1 else self.deck2
        return sum(i * c for i, c in enumerate(reversed(winning_deck), start=1))


# 22-1
input_ = get_input(day=22, as_list=False)
game = RecursiveCombat.parse(input_)
game.play(recursive=False)
print(game.score)

# 22-2
game = RecursiveCombat.parse(input_)
game.play(recursive=True)
print(game.score)
