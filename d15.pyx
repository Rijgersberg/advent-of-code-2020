import time

from cpython cimport array
import array


cdef solve(input_, int max_turn):
    t0 = time.time()
    cdef int i, n, prev, c

    cdef int[:] numbers = array.array('i', [-1] * (max_turn + len(input_)))

    for i, n in enumerate(input_[:-1]):
        numbers[n] = i

    t1 = time.time()

    prev = input_[-1]
    for i in range(len(input_) - 1, max_turn - 1):
        c = numbers[prev]
        if c != -1:
            numbers[prev], prev = i, i - c
        else:
            numbers[prev], prev = i, 0
    t2 = time.time()
    print(f'Time for setup: {t1 - t0}, time for loop: {t2 - t1}')
    return prev

assert solve([0, 3, 6], 10) == 0

puzzle_input = array.array('i', [18,8,0,5,4,1,20])

t0 = time.time()
print(solve(puzzle_input, 2020), f'in {time.time() - t0} seconds')

t0 = time.time()
print(solve(puzzle_input, 30000000), f'in {time.time() - t0} seconds')
