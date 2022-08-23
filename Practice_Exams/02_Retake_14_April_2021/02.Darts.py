player_1, player_2 = input().split(", ")

matrix = [input().split() for x in range(7)]

player_1_points = 501
player_2_points = 501
player_1_throws = 0
player_2_throws = 0

turn_counter = 1

while True:
    hit_row, hit_col = [int(x) for x in input().strip('()').split(', ')]
    hit_points = 0

    try:
        if matrix[hit_row][hit_col].isdigit():
            hit_points += int(matrix[hit_row][hit_col])
        elif matrix[hit_row][hit_col] == 'D':
            for row in range(len(matrix)):
                if matrix[row][hit_col].isdigit():
                    hit_points += int(matrix[row][hit_col])
            for col in range(len(matrix)):
                if matrix[hit_row][col].isdigit():
                    hit_points += int(matrix[hit_row][col])
            hit_points *= 2
        elif matrix[hit_row][hit_col] == 'T':
            for row in range(len(matrix)):
                if matrix[row][hit_col].isdigit():
                    hit_points += int(matrix[row][hit_col])
            for col in range(len(matrix)):
                if matrix[hit_row][col].isdigit():
                    hit_points += int(matrix[hit_row][col])
            hit_points *= 3
        elif matrix[hit_row][hit_col] == 'B':
            hit_points = 501

    except IndexError:
        hit_points = 0

    if turn_counter % 2 != 0:
        player_1_points -= hit_points
        player_1_throws += 1
    else:
        player_2_points -= hit_points
        player_2_throws += 1

    turn_counter += 1

    if player_1_points <= 0:
        print(f"{player_1} won the game with {player_1_throws} throws!")
        break
    if player_2_points <= 0:
        print(f"{player_2} won the game with {player_2_throws} throws!")
        break
