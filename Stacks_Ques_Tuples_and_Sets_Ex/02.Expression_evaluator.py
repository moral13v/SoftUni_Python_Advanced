from collections import deque

line = deque(input().split())
result = 0
operators = ['+', '-', '*', '/']

while len(line) != 1:

    num1 = None
    num2 = None
    num3 = None

    num1 = int(line[0])
    line.popleft()
    if line[0] not in operators:
        num2 = int(line[0])
        line.popleft()
    if line[0] not in operators:
        num3 = int(line[0])
        line.popleft()
    op = line[0]
    line.popleft()

    if op == "-":
        if num3:
            result = num1 - num2 - num3
        else:
            result = num1 - num2
    elif op == "+":
        if num3:
            result = num1 + num2 + num3
        else:
            result = num1 + num2
    elif op == "*":
        if num3:
            result = num1 * num2 * num3
        else:
            result = num1 * num2
    elif op == "/":
        if num3:
            result = num1 / num2 / num3
        else:
            result = num1 / num2

    line.appendleft(result)

print(int(result))
