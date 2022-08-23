def is_knight(row_index, col_index, collection):
    return collection[row_index][col_index] == "K"


def in_range(row_index, col_index, length):
    return 0 <= row_index <= length - 1 and 0 <= col_index <= length - 1


def position_counter(row_index, col_index, collection):
    result = 0
    if in_range(row_index - 2, col_index + 1, len(collection)) and is_knight(row_index - 2, col_index + 1, collection):
        result += 1
    if in_range(row_index - 1, col_index + 2, len(collection)) and is_knight(row_index - 1, col_index + 2, collection):
        result += 1
    if in_range(row_index + 1, col_index + 2, len(collection)) and is_knight(row_index + 1, col_index + 2, collection):
        result += 1
    if in_range(row_index + 2, col_index + 1, len(collection)) and is_knight(row_index + 2, col_index + 1, collection):
        result += 1
    if in_range(row_index + 2, col_index - 1, len(collection)) and is_knight(row_index + 2, col_index - 1, collection):
        result += 1
    if in_range(row_index + 1, col_index - 2, len(collection)) and is_knight(row_index + 1, col_index - 2, collection):
        result += 1
    if in_range(row_index - 1, col_index - 2, len(collection)) and is_knight(row_index - 1, col_index - 2, collection):
        result += 1
    if in_range(row_index - 2, col_index - 1, len(collection)) and is_knight(row_index - 2, col_index - 1, collection):
        result += 1

    return result


size = int(input())
matrix = []
for _ in range(size):
    matrix.append(list(input()))
removed_knights = 0

while True:
    table = {}

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "0":
                continue
            counter = position_counter(row, col, matrix)
            if counter:
                table[(row, col)] = counter

    if len(table) == 0:
        break

    best_counter = 0
    knight_row, knight_col = 0, 0
    for coordinates, counter in table.items():
        if counter > best_counter:
            best_counter = counter
            knight_row = coordinates[0]
            knight_col = coordinates[1]
    matrix[knight_row][knight_col] = '0'
    removed_knights += 1

print(removed_knights)
