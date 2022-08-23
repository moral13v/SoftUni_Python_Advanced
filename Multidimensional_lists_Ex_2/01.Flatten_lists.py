line = input().split("|")
result = []

for i in range(len(line) - 1, - 1, - 1):
    result.extend(line[i].split())

print(*result, sep=" ")
