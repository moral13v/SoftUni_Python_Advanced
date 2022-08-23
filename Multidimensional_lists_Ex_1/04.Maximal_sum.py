rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
max_sum = 0
sub_matrix = []


for row in range(rows - 2):
    for col in range(cols - 2):
        curr_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] +\
                   matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] +\
                   matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]

        if curr_sum >= max_sum:
            max_sum = curr_sum
            curr_sum = 0
            sub_matrix = [
                [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
                [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
                [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
            ]

print(f"Sum = {max_sum}")
for el in sub_matrix:
    print(" ".join([str(x) for x in el]))
