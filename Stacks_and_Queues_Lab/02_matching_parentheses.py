data = input()

par_stack = []

for i in range(len(data)):
    if data[i] == "(":
        par_stack.append(i)
    elif data[i] == ")":
        start_index = par_stack.pop()
        print(data[start_index: i+1])
