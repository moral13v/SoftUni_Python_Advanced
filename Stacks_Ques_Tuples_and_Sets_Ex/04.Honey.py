from collections import deque


def calculation(bee, nectar, symbol):
    result = 0
    if symbol == '+':
        result = bee + nectar
    elif symbol == '-':
        result = bee - nectar
    elif symbol == '*':
        result = bee * nectar
    elif symbol == '/' and nectar > 0:
        result = bee / nectar
    return abs(result)


bees = deque(int(x) for x in input().split())
nectar_stack = [int(x) for x in input().split()]
operators = deque(input().split())
total_honey = 0


while bees and nectar_stack:
    curr_bee = bees.popleft()
    curr_nectar = nectar_stack.pop()

    if curr_nectar < curr_bee:
        bees.appendleft(curr_bee)
        continue
    else:
        operator = operators.popleft()
        honey = calculation(curr_bee, curr_nectar, operator)
        total_honey += honey

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
elif nectar_stack:
    print(f"Nectar left: {', '.join([str(x) for x in nectar_stack])}")
