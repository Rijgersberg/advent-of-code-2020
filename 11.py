import copy

from aoc import get_input

# game of ~life~ thrones.
game_str = get_input(day=11)
N, M = len(game_str[0]), len(game_str)

game = {x: {} for x in range(N)}
for y, line in enumerate(game_str):
    for x, c in enumerate(line):
        game[x][y] = c

original_game = copy.deepcopy(game)
DIRECTIONS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


# 11-1
def neighbors(x, y, way='close'):
    if way == 'close':
        yield from ((x + dx, y + dy) for dx, dy in DIRECTIONS
                    if 0 <= x + dx < N and 0 <= y + dy < M)
    elif way == 'visible':
        yield from visible_neighbors[(x, y)]


def step(old_game, threshold, way):
    game = copy.deepcopy(old_game)
    for x in range(N):
        for y in range(M):
            seat = old_game[x][y]
            if seat != '.':
                adj_seats = sum(old_game[i][j] == '#' for i, j in neighbors(x, y, way))
                if seat == 'L':
                    if adj_seats == 0:
                        game[x][y] = '#'
                elif seat == '#':
                    if adj_seats >= threshold:
                        game[x][y] = 'L'
    return game


def play(game, threshold, way):
    t = 0
    while True:
        t += 1
        new_game = step(copy.deepcopy(game), threshold, way)
        if new_game == game:
            return t, sum(sum([c == '#' for c in row.values()])
                          for row in game.values())
        game = new_game


def find_first_visible(x, y, dir, game):
    new_x, new_y = x + dir[0], y + dir[1]
    if 0 <= new_x < N and 0 <= new_y < M:
        c = game[new_x][new_y]
        if c in ['L', '#']:
            return new_x, new_y
        else:
            return find_first_visible(new_x, new_y, dir, game)
    else:
        return None

def make_visible_neighbors(game):
    neighbor_lookup = {}
    for x in range(N):
        for y in range(M):
            neighbors = []
            for dir in DIRECTIONS:
                neighbor = find_first_visible(x, y, dir, game)
                if neighbor is not None:
                    neighbors.append(neighbor)
            neighbor_lookup[(x, y)] = neighbors
    return neighbor_lookup


# 11-1
t, occupied = play(game, threshold=4, way='close')
print(f'{t=}, {occupied=}')

# 11-2
visible_neighbors = make_visible_neighbors(original_game)
t, occupied = play(original_game, threshold=5, way='visible')
print(f'{t=}, {occupied=}')
