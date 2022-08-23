from collections import deque

chocolate_stack = [int(x) for x in input().split(", ")]
milk_cups = deque([int(x) for x in input().split(", ")])
milkshakes = 0

while milkshakes < 5 and chocolate_stack and milk_cups:

    if chocolate_stack[-1] <= 0 or milk_cups[0] <= 0:
        if chocolate_stack[-1] <= 0:
            chocolate_stack.pop()
        if milk_cups[0] <= 0:
            milk_cups.popleft()
        continue

    if chocolate_stack[-1] == milk_cups[0]:
        milkshakes += 1
        chocolate_stack.pop()
        milk_cups.popleft()
    else:
        chocolate_stack[-1] -= 5
        milk_cups.append(milk_cups.popleft())

if milkshakes >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate_stack:
    print(f"Chocolate: {', '.join([str(x) for x in chocolate_stack])}")
else:
    print("Chocolate: empty")

if milk_cups:
    print(f"Milk: {', '.join([str(x) for x in milk_cups])}")
else:

    print("Milk: empty")



