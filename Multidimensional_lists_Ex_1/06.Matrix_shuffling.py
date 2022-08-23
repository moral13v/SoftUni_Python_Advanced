rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]
command = input()

while command != "END":
    command_args = command.split()
    valid_command = False
    if len(command_args) == 5 and command_args[0] == "swap":
        row1, col1, row2, col2 = [int(x) for x in command_args[1:]]
        if row1 <= rows and row2 <= rows and col1 <= cols and col2 <= cols\
                and row1 >= 0 and row2 >= 0 and col1 >= 0 and col2 >= 0:
            valid_command = True
            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            for row in matrix:
                print(" ".join(row))
    if not valid_command:
        print("Invalid input!")
    command = input()
