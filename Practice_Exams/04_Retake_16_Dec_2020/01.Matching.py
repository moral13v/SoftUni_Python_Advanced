from collections import deque

males = [int(x) for x in input().split() if int(x) > 0]
females = deque(int(x) for x in input().split() if int(x) > 0)
matches_counter = 0

while males and females:
    if males[-1] % 25 == 0:
        males.pop()
        try:
            males.pop()
            continue
        except IndexError:
            continue

    if females[0] % 25 == 0:
        females.popleft()
        try:
            females.popleft()
            continue
        except IndexError:
            continue

    if males[-1] == females[0]:
        males.pop()
        females.popleft()
        matches_counter += 1
    else:
        females.popleft()
        males[-1] -= 2
        if males[-1] <= 0:
            males.pop()
        elif males[-1] % 25 == 0:
            males.pop()
            try:
                males.pop()
            except IndexError:
                pass

print(f"Matches: {matches_counter}")

if males:
    print(f"Males left: {', '.join([str(x) for x in reversed(males)])}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join([str(x) for x in females])}")
else:
    print("Females left: none")
