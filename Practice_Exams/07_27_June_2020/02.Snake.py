def move_up(row, col):
    return row - 1, col


def move_down(row, col):
    return row + 1, col


def move_left(row, col):
    return row, col - 1


def move_right(row, col):
    return row, col + 1


moves = {'up': move_up,
         'down': move_down,
         'right': move_right,
         'left': move_left}


size = int(input())

matrix = [[x for x in input()] for x in range(size)]

snake_row = 0
snake_col = 0

for row in range(size):
    for col in range(size):
        if matrix[row][col] == 'S':
            snake_row, snake_col = row, col

food = 0

while food < 10:
    command = input()
    matrix[snake_row][snake_col] = '.'
    for key, value in moves.items():
        if command == key:
            snake_row, snake_col = value(snake_row, snake_col)

    if snake_row >= size or snake_row < 0 or snake_col >= size or snake_col < 0:
        print("Game over!")
        break

    elif matrix[snake_row][snake_col] == '*':
        food += 1
        matrix[snake_row][snake_col] = 'S'
    elif matrix[snake_row][snake_col] == 'B':
        matrix[snake_row][snake_col] = '.'
        for row in range(size):
            for col in range(size):
                if matrix[row][col] == 'B':
                    snake_row, snake_col = row, col
                    matrix[snake_row][snake_col] = 'S'


if food >= 10:
    print("You won! You fed the snake.")

print(f"Food eaten: {food}")

for row in matrix:
    print(''.join(row))
