n = int(input())

matrix = [input().split() for _ in range(n)]

alice_row = 0
alice_col = 0

for row in range(n):
    for col in range(n):
        if matrix[row][col] == 'A':
            alice_row = row
            alice_col = col

collected_tea = 0
enough_tee = False

while True:

    if alice_row < 0 or alice_col < 0 or alice_row >= n or alice_col >= n:
        break

    if matrix[alice_row][alice_col] == 'R':
        matrix[alice_row][alice_col] = '*'
        break

    if matrix[alice_row][alice_col].isnumeric():
        collected_tea += int(matrix[alice_row][alice_col])
        matrix[alice_row][alice_col] = '*'
    else:
        matrix[alice_row][alice_col] = '*'

    if collected_tea >= 10:
        enough_tee = True
        break

    command = input()

    if command == 'up':
        alice_row -= 1
    elif command == 'down':
        alice_row += 1
    elif command == 'left':
        alice_col -= 1
    elif command == 'right':
        alice_col += 1

if enough_tee:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(*row, sep=" ")
