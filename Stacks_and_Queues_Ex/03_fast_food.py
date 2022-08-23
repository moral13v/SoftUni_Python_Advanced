from collections import deque

food = int(input())
orders = deque(map(int, input().split()))

print(max(orders))

while orders:
    current_order = orders[0]
    if current_order > food:
        break
    else:
        food -= orders.popleft()

if orders:
    print(f"Orders left: {' '.join(map(str, orders))}")
else:
    print("Orders complete")


