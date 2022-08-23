set_a = {int(x) for x in input().split()}
set_b = {int(x) for x in input().split()}

n = int(input())

for _ in range(n):
    command = input().split()
    numbers = {int(x) for x in command[2::]}
    if command[0] == "Add":
        if command[1] == "First":
            set_a = set_a.union(numbers)
        elif command[1] == "Second":
            set_b = set_b.union(numbers)
    elif command[0] == "Remove":
        if command[1] == "First":
            set_a.difference_update(numbers)
        elif command[1] == "Second":
            set_b.difference_update(numbers)
    elif "Check" in command:
        sub = False
        if set_a.issubset(set_b):
            sub = True
        elif set_b.issubset(set_a):
            sub = True
        print(sub)

print(", ".join([str(x) for x in sorted(set_a)]))
print(", ".join([str(x) for x in sorted(set_b)]))
