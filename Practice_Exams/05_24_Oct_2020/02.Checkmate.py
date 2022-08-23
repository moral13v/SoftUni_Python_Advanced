size = 8
matrix = [input().split() for x in range(size)]

queen_threats = []

king_row = 0
king_col = 0

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == 'K':
            king_row, king_col = row, col


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

for move in moves:
    current_row, current_col = king_row, king_col
    while True:
        next_row, next_col = move(current_row, current_col)
        if next_row < 0 or next_row >= size or next_col < 0 or next_col >= size:
            break
        if matrix[next_row][next_col] == 'Q' and next_col >= 0 and next_row >= 0:
            queen_threats.append([next_row, next_col])
            break

        current_row, current_col = next_row, next_col

if not queen_threats:
    print('The king is safe!')
else:
    for queen in queen_threats:
        print(queen)

