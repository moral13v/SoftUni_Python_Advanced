data = list(input())

# stack = [data[i] for i in range(len(data) - 1, -1, -1)]

stack = []

for i in range(len(data)):
    stack.append(data.pop())

print("".join(stack))
