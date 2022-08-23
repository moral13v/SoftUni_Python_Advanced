from collections import deque

circle = deque(input().split())
n = int(input())

while len(circle) > 1:
    circle.rotate(-n)
    print(f"Removed {circle.pop()}")

print(f"Last is {circle.pop()}")