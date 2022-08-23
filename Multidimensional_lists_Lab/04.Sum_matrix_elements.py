rows, cols = [int(x) for x in input().split(", ")]

matrix = [[int(x) for x in input().split()] for row in range(rows)]

for col in range(cols):
    col_sum = 0
    for row in range(rows):
        col_sum += matrix[row][col]
    print(col_sum)
