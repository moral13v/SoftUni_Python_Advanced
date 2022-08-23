data = input().split()

rev_num_stack = []

for i in range(len(data)):
    rev_num_stack.append(data.pop())

print(" ".join(rev_num_stack))
