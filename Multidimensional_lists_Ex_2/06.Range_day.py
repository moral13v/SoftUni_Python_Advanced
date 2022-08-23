size = 5
matrix = [input().split() for _ in range(size)]
targets = 0
hit_targets = []
shooter_row = 0
shooter_col = 0

for row in range(size):
    for col in range(size):
        if matrix[row][col] == 'x':
            targets += 1
        elif matrix[row][col] == 'A':
            shooter_row, shooter_col = row, col

n = int(input())

for _ in range(n):

    if not targets:
        break

    command = input().split()
    action = command[0]
    direction = command[1]

    if action == "move":
        new_row = shooter_row
        new_col = shooter_col
        steps = int(command[2])
        if direction == "up":
            new_row = shooter_row - steps
        elif direction == "down":
            new_row = shooter_row + steps
        elif direction == "left":
            new_col = shooter_col - steps
        elif direction == "right":
            new_col = shooter_col + steps

        if new_row < 0 or new_col < 0 or new_row >= size or new_col >= size:
            new_row = shooter_row
            new_col = shooter_col
        elif matrix[new_row][new_col] != '.':
            new_row = shooter_row
            new_col = shooter_col
        else:
            shooter_row = new_row
            shooter_col = new_col

    elif action == "shoot":
        shot = 1
        shot_row = shooter_row
        shot_col = shooter_col

        while True:

            if direction == "up":
                shot_row -= shot
            elif direction == "down":
                shot_row += shot
            elif direction == "left":
                shot_col -= shot
            elif direction == "right":
                shot_col += shot

            if shot_row < 0 or shot_col < 0 or shot_row >= size or shot_col >= size:
                break

            if matrix[shot_row][shot_col] != 'x':
                continue
            elif matrix[shot_row][shot_col] == 'x':
                targets -= 1
                hit_targets.append([shot_row, shot_col])
                matrix[shot_row][shot_col] = '.'
                break


if targets:
    print(f"Training not completed! {targets} targets left.")
else:
    print(f"Training completed! All {len(hit_targets)} targets hit.")

print(*hit_targets, sep='\n')
