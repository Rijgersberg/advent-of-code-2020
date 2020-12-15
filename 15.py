def solve(input_, max_turn):
    rest, last = input_[:-1], input_[-1]

    numbers = {n: i for i, n in enumerate(rest)}

    init = len(numbers)
    i = init
    prev = last
    while i < max_turn - 1:
        if prev in numbers:
            n_turns_apart = i - numbers[prev]
            numbers[prev] = i
            prev = n_turns_apart
        else:
            numbers[prev] = i
            prev = 0
        i += 1
    return (i + 1, prev)

puzzle_input = [18,8,0,5,4,1,20]
assert solve([0, 3, 6], 10) == (10, 0)

print(solve(puzzle_input, 2020))
print(solve(puzzle_input, 30000000))
