def is_valid(row_index, col_index, length):
    if 0 <= row_index <= length - 1 and 0 <= col_index <= length - 1:
        return True
    return False


def result(operation, a, b, c, collection):
    a = int(a)
    b = int(b)
    c = int(c)
    if operation == "Add":
        collection[a][b] += c
    elif operation == "Subtract":
        collection[a][b] -= c
    return collection[a][b]


size = int(input())

matrix = [[int(x) for x in input().split()] for x in range(size)]

command = input()

while command != "END":
    action, row, col, value = command.split()
    if is_valid(int(row), int(col), size):
        result(action, row, col, value, matrix)
    else:
        print("Invalid coordinates")

    command = input()

for el in matrix:
    print(*el, sep=" ")
