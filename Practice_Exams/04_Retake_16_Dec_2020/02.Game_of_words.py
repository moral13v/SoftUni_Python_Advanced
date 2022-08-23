string = input()

size = int(input())

matrix = [list(input()) for x in range(size)]

player_row = 0
player_col = 0

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == 'P':
            player_row, player_col = row, col

m = int(input())

for _ in range(m):
    command = input()

    matrix[player_row][player_col] = '-'
    prev_row, prev_col = player_row, player_col

    if command == "up":
        player_row -= 1
    elif command == "down":
        player_row += 1
    elif command == "left":
        player_col -= 1
    elif command == "right":
        player_col += 1

    if player_row < 0 or player_row >= size or player_col < 0 or player_col >= size:
        if string:
            string = string[:-1]
            player_row, player_col = prev_row, prev_col
    else:
        if matrix[player_row][player_col].isalpha():
            string += matrix[player_row][player_col]

    matrix[player_row][player_col] = 'P'

print(string)
for row in matrix:
    print(''.join(row))
