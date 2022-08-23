rows, cols = [int(x) for x in input().split()]

snake = input()
snake_index = 0

matrix = [[None for _ in range(cols)] for _ in range(rows)]

for row in range(rows):
    if row % 2 == 0:
        for col in range(cols):
            matrix[row][col] = snake[snake_index - len(snake)]
            snake_index += 1
            if snake_index == len(snake):
                snake_index = 0
    else:
        for col in range(cols - 1, -1, -1):
            matrix[row][col] = snake[snake_index - len(snake)]
            snake_index += 1
            if snake_index == len(snake):
                snake_index = 0

for row in matrix:
    print(*row, sep='')
