n = int(input())

matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]
primary_diagonal = []
sec_diagonal = []

for i in range(n):
    row = i
    col_for_p = i
    col_for_s = n - 1 - i
    primary_diagonal.append(matrix[row][col_for_p])
    sec_diagonal.append(matrix[row][col_for_s])

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in sec_diagonal])}. Sum: {sum(sec_diagonal)}")
