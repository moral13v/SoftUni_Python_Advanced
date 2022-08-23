n = int(input())

stack = []

for i in range(n):
    data = input().split()
    query = data[0]
    if query == "1":
        stack.append(int(data[1]))
    elif query == "2":
        if stack:
            stack.pop()
    elif query == "3":
        if stack:
            print(max(stack))
    elif query == "4":
        if stack:
            print(min(stack))

rev_stack = []

while stack:
    rev_stack.append(str(stack.pop()))

print(", ".join(rev_stack))
