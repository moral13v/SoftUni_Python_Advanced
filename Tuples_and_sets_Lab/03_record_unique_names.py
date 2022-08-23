n = int(input())

names = []
for i in range(n):
    names.append(input())
unique_names = {name for name in names}
[print(name) for name in unique_names]

