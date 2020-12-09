import time
from itertools import accumulate, combinations

from aoc import get_input

code = [int(line) for line in get_input(day=9)]

# 9-1
N = 25
i = N
for i in range(N, len(code)):
    if not code[i] in {sum(c) for c in combinations(code[i-N:i], 2)}:
        target = code[i]
        print(target)
        break

# 9-2 slow
t0 = time.time()
for i in range(len(code)):
    j = i + 1
    running_total = code[i]
    while j < len(code) and running_total < target:
        running_total += code[j]
        if running_total == target:
            print(i, j, min(code[i:j+1]) + max(code[i:j+1]))
            break
        j += 1
print(f'{time.time() - t0} seconds')

# 9-2 fast
t0 = time.time()
cumsum = list(accumulate(code))
i, j = 0, 0
while i < len(code) and j < len(code):
    test_sum = cumsum[j] - cumsum[i]  # difference between entries in cumsum == sum over the range between the entries
    if test_sum == target:
        print(i, j, min(code[i:j + 1]) + max(code[i:j + 1]))
        break
    elif test_sum < target:
        j += 1
    elif test_sum > target:
        i += 1
print(f'{time.time() - t0} seconds')
