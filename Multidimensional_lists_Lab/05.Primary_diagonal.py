n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]
primary_diagonal_sum = 0
secondary_diagonal_sum = 0

for row in range(n):
    col = row
    primary_diagonal_sum += matrix[row][col]

for row in range(n - 1, -1, -1):
    col = n - 1 - row
    secondary_diagonal_sum += matrix[row][col]

print(primary_diagonal_sum)
# print(secondary_diagonal_sum)
