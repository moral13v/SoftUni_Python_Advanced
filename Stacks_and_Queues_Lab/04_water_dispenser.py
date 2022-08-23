from collections import deque

water = int(input())
data = input()
line = deque()

while data != "Start":
    name = data
    line.append(name)
    data = input()

data = input()

while data != "End":
    if data.isdigit():
        quantity = int(data)
        if quantity <= water:
            print(f"{line.popleft()} got water")
            water -= quantity
        else:
            print(f"{line.popleft()} must wait")
    else:
        command, quantity = data.split()
        water += int(quantity)
    data = input()

print(f"{water} liters left")
