rows = int(input())
flattened_matrix = []

# matrix = [[int(x) for x in input().split(", ")] for i in range(rows)]
#
# for el in matrix:
#     flattened_matrix.extend(el)

for i in range(rows):
    flattened_matrix.extend([int(x) for x in input().split(", ")])

print(flattened_matrix)
