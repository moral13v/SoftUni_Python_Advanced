clothes_stack = [int(item) for item in input().split()]
rack_capacity = int(input())
rack_count = 1
current_rack = rack_capacity

while clothes_stack:
    if clothes_stack[-1] <= current_rack:
        current_rack -= clothes_stack.pop()
    else:
        rack_count += 1
        current_rack = rack_capacity

print(rack_count)
