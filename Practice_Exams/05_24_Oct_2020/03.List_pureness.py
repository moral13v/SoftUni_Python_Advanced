def best_list_pureness(*args):
    from collections import deque

    numbers = deque(int(x) for x in args[0])
    k = args[1]
    pureness = 0
    best_pureness = -float('inf')
    best_rotation = 0

    for rotation in range(k + 1):
        for i in range(len(numbers)):
            pureness += i * numbers[i]
        if pureness > best_pureness:
            best_pureness = pureness
            best_rotation = rotation

        numbers.appendleft(numbers.pop())
        pureness = 0

    return f"Best pureness {best_pureness} after {best_rotation} rotations"
