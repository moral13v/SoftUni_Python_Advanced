rows, cols = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]
max_sum = 0
sub_matrix = []


for row in range(rows - 1):
    for col in range(cols - 1):
        curr_sum = matrix[row][col] + matrix[row][col + 1] + \
           matrix[row + 1][col] + matrix[row + 1][col + 1]
        if curr_sum > max_sum:
            max_sum = curr_sum
            curr_sum = 0
            sub_matrix = [[matrix[row][col], matrix[row][col + 1]], [matrix[row + 1][col], matrix[row + 1][col + 1]]]

for el in sub_matrix:
    print(" ".join([str(x) for x in el]))

print(max_sum)