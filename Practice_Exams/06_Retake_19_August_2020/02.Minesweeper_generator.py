def move_up(row, col):
    return row - 1, col


def move_down(row, col):
    return row + 1, col


def move_left(row, col):
    return row, col - 1


def move_right(row, col):
    return row, col + 1


def move_up_left(row, col):
    return row - 1, col - 1


def move_down_left(row, col):
    return row + 1, col - 1


def move_up_right(row, col):
    return row - 1, col + 1


def move_down_right(row, col):
    return row + 1, col + 1


moves = [move_up, move_down, move_left, move_right, move_up_right, move_down_right, move_up_left, move_down_left]


size = int(input())
matrix = [[0 for x in range(size)] for y in range(size)]


bombs_count = int(input())

for _ in range(bombs_count):
    bomb_row, bomb_col = input().strip('()').split(', ')
    matrix[int(bomb_row)][int(bomb_col)] = '*'

for row in range(size):
    for col in range(size):
        if matrix[row][col] != '*':
            for move in moves:
                next_row, next_col = move(row, col)
                if next_row < 0 or next_row >= size or next_col < 0 or next_col >= size:
                    continue
                if matrix[next_row][next_col] == '*' and next_col >= 0 and next_row >= 0:
                    matrix[row][col] += 1

for row in matrix:
    print(' '.join([str(x) for x in row]))


