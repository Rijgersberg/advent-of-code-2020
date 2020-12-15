def solve(input_, max_turn):
    numbers = {n: i for i, n in enumerate(input_[:-1])}

    prev = input_[-1]
    for i in range(len(numbers), max_turn - 1):
        if prev in numbers:
            numbers[prev], prev = i, i - numbers[prev]
        else:
            numbers[prev], prev = i, 0
    return (i + 2, prev)

puzzle_input = [18,8,0,5,4,1,20]
assert solve([0, 3, 6], 10) == (10, 0)

print(solve(puzzle_input, 2020))
print(solve(puzzle_input, 30000000))
