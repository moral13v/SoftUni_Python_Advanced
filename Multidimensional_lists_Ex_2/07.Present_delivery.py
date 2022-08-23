def get_next_position(direction, row, col):
    if direction == "up":
        return row - 1, col
    if direction == "down":
        return row + 1, col
    if direction == "left":
        return row, col - 1
    if direction == "right":
        return row, col + 1


presents = int(input())
size = int(input())

matrix = [input().split() for _ in range(size)]

nice_kids = 0
presents_to_nice_kids = 0
santa_row = 0
santa_col = 0


for row in range(size):
    for col in range(size):
        if matrix[row][col] == 'V':
            nice_kids += 1
        elif matrix[row][col] == 'S':
            santa_row = row
            santa_col = col

while True:
    command = input()
    if command == "Christmas morning":
        break

    matrix[santa_row][santa_col] = '-'

    santa_row, santa_col = get_next_position(command, santa_row, santa_col)
    if matrix[santa_row][santa_col] == 'V':
        presents -= 1
        presents_to_nice_kids += 1

    elif matrix[santa_row][santa_col] == 'C':

        if matrix[santa_row][santa_col - 1] == 'V' and presents:
            presents -= 1
            presents_to_nice_kids += 1
            matrix[santa_row][santa_col - 1] = '-'
        elif matrix[santa_row][santa_col - 1] == 'X' and presents:
            presents -= 1
            matrix[santa_row][santa_col - 1] = '-'

        if matrix[santa_row][santa_col + 1] == 'V' and presents:
            presents -= 1
            presents_to_nice_kids += 1
            matrix[santa_row][santa_col + 1] = '-'
        elif matrix[santa_row][santa_col + 1] == 'X' and presents:
            presents -= 1
            matrix[santa_row][santa_col + 1] = '-'

        if matrix[santa_row - 1][santa_col] == 'V' and presents:
            presents -= 1
            presents_to_nice_kids += 1
            matrix[santa_row - 1][santa_col] = '-'
        elif matrix[santa_row - 1][santa_col] == 'X' and presents:
            presents -= 1
            matrix[santa_row - 1][santa_col] = '-'

        if matrix[santa_row + 1][santa_col] == 'V' and presents:
            presents -= 1
            presents_to_nice_kids += 1
            matrix[santa_row + 1][santa_col] = '-'
        elif matrix[santa_row + 1][santa_col] == 'X' and presents:
            presents -= 1
            matrix[santa_row + 1][santa_col] = '-'

    matrix[santa_row][santa_col] = 'S'

    if presents == 0 or presents_to_nice_kids == nice_kids:
        break

if presents == 0 and presents_to_nice_kids < nice_kids:
    print("Santa ran out of presents!")

for row in matrix:
    print(*row, sep=' ')

if presents_to_nice_kids == nice_kids:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - presents_to_nice_kids} nice kid/s.")

