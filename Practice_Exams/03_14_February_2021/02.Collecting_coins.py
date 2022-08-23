size = int(input())

matrix = [input().split() for _ in range(size)]

coins = 0
player_row = 0
player_col = 0
game_over = False

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "P":
            player_row, player_col = row, col

player_path = [[player_row, player_col]]

while coins < 100:
    command = input()

    if command == "up":
        if player_row == 0:
            player_row = size - 1
        else:
            player_row -= 1
    elif command == "down":
        if player_row == size - 1:
            player_row = 0
        else:
            player_row += 1
    elif command == "left":
        if player_col == 0:
            player_col = size - 1
        else:
            player_col -= 1
    elif command == "right":
        if player_col == size - 1:
            player_col = 0
        else:
            player_col += 1

    player_position = matrix[player_row][player_col]
    player_path.append([player_row, player_col])

    if player_position.isdigit():
        coins += int(player_position)
        matrix[player_row][player_col] = '.'
    elif player_position == 'X':
        coins //= 2
        game_over = True
        break

if game_over:
    print(f"Game over! You've collected {coins} coins.")
else:
    print(f"You won! You've collected {coins} coins.")

print("Your path:")

for position in player_path:
    print(position)
