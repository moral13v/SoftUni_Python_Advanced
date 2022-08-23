def move_up(row, col):
    return row - 1, col


def move_down(row, col):
    return row + 1, col


def move_up_right(row, col):
    return row - 1, col + 1


def move_up_left(row, col):
    return row - 1, col - 1


def move_down_right(row, col):
    return row + 1, col + 1


def move_down_left(row, col):
    return row + 1, col - 1


white_attack_moves = [move_up_left, move_up_right]
black_attack_moves = [move_down_left, move_down_right]


matrix = [input().split() for x in range(8)]

white_row = 0
white_col = 0

black_row = 0
black_col = 0

white_wins = False
white_queen = False

black_wins = False
black_queen = False

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] == 'w':
            white_row, white_col = row, col
        elif matrix[row][col] == 'b':
            black_row, black_col = row, col

while True:
    attack_row = 0
    attack_col = 0

    if white_col == 0:
        attack_row, attack_col = move_up_right(white_row, white_col)
        if matrix[attack_row][attack_col] == 'b':
            white_wins = True
            matrix[white_row][white_col] = '-'
            white_row, white_col = attack_row, attack_col
            matrix[white_row][white_col] = 'w'
            break
    elif white_col == 7:
        attack_row, attack_col = move_up_left(white_row, white_col)
        if matrix[attack_row][attack_col] == 'b':
            white_wins = True
            matrix[white_row][white_col] = '-'
            white_row, white_col = attack_row, attack_col
            matrix[white_row][white_col] = 'w'
            break
    else:
        for move in white_attack_moves:
            attack_row, attack_col = move(white_row, white_col)
            if matrix[attack_row][attack_col] == 'b':
                white_wins = True
                matrix[white_row][white_col] = '-'
                white_row, white_col = attack_row, attack_col
                matrix[white_row][white_col] = 'w'
                break

    if white_wins or black_wins:
        break

    matrix[white_row][white_col] = '-'
    white_row, white_col = move_up(white_row, white_col)
    matrix[white_row][white_col] = 'w'

    if black_col == 0:
        attack_row, attack_col = move_down_right(black_row, black_col)
        if matrix[attack_row][attack_col] == 'w':
            black_wins = True
            matrix[black_row][black_col] = '-'
            black_row, black_col = attack_row, attack_col
            matrix[black_row][black_col] = 'b'
            break
    elif black_col == 7:
        attack_row, attack_col = move_down_left(black_row, black_col)
        if matrix[attack_row][attack_col] == 'w':
            black_wins = True
            matrix[black_row][black_col] = '-'
            black_row, black_col = attack_row, attack_col
            matrix[black_row][black_col] = 'b'
            break
    else:
        for move in black_attack_moves:
            attack_row, attack_col = move(black_row, black_col)
            if matrix[attack_row][attack_col] == 'w':
                black_wins = True
                matrix[black_row][black_col] = '-'
                black_row, black_col = attack_row, attack_col
                matrix[black_row][black_col] = 'b'
                break

    if white_wins or black_wins:
        break

    matrix[black_row][black_col] = '-'
    black_row, black_col = move_down(black_row, black_col)
    matrix[black_row][black_col] = 'b'

    if white_row == 0:
        white_wins = True
        white_queen = True
        break
    if black_row == 7:
        black_wins = True
        black_queen = True
        break


if white_wins:
    if white_queen:
        print(f"Game over! White pawn is promoted to a queen at {chr(97 + white_col)}{abs(8 - white_row)}.")
    else:
        print(f"Game over! White win, capture on {chr(97 + white_col)}{abs(8 - white_row)}.")

if black_wins:
    if black_queen:
        print(f"Game over! Black pawn is promoted to a queen at {chr(97 + black_col)}{abs(8 - black_row)}.")
    else:
        print(f"Game over! Black win, capture on {chr(97 + black_col)}{abs(8 - black_row)}.")

