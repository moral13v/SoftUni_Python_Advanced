def move_up(row_index, col_index):
    return row_index - 1, col_index


def move_down(row_index, col_index):
    return row_index + 1, col_index


def move_right(row_index, col_index):
    return row_index, col_index + 1


def move_left(row_index, col_index):
    return row_index, col_index - 1


size = int(input())

field = [input().split() for i in range(size)]

bunny_row = 0
bunny_col = 0

for row in range(size):
    for col in range(size):
        if field[row][col] == 'B':
            bunny_row = row
            bunny_col = col

directions = {"up": move_up, "down": move_down, "left": move_left, "right": move_right}

best_dir = ''
best_score = float('-inf')
best_path = []

for direction, step in directions.items():
    current_row, current_col = bunny_row, bunny_col
    current_score = 0
    path = []

    while True:
        current_row, current_col = step(current_row, current_col)
        if current_row < 0 or current_col < 0 or current_row >= size or current_col >= size:
            break

        if field[current_row][current_col] == 'X':
            break

        path.append([current_row, current_col])
        current_score += int(field[current_row][current_col])

    if current_score >= best_score:
        best_score = current_score
        best_dir = direction
        best_path = path

print(best_dir)
for step in best_path:
    print(step)
print(best_score)
