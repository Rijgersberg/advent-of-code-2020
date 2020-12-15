def solve(input_, max_turn):
    rest, last = input_[:-1], input_[-1]

    numbers = {n: i for i, n in enumerate(rest)}

    i = len(numbers)
    prev = last
    for i in range(len(numbers), max_turn - 1):
        if prev in numbers:
            n_turns_apart = i - numbers[prev]
            numbers[prev] = i
            prev = n_turns_apart
        else:
            numbers[prev] = i
            prev = 0
    return (i + 2, prev)

puzzle_input = [18,8,0,5,4,1,20]
assert solve([0, 3, 6], 10) == (10, 0)

print(solve(puzzle_input, 2020))
print(solve(puzzle_input, 30000000))
