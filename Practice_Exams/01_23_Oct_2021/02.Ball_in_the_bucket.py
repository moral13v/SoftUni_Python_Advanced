matrix = [input().split() for x in range(6)]
result = 0

for _ in range(3):
    throw_row, throw_col = [int(x) for x in input().strip('()').split(', ')]
    try:
        if matrix[throw_row][throw_col] == 'B':
            for row in range(len(matrix)):
                if matrix[row][throw_col].isdigit():
                    result += int(matrix[row][throw_col])
            matrix[throw_row][throw_col] = '.'
    except IndexError:
        continue

if 100 <= result <= 199:
    print(f"Good job! You scored {result} points, and you've won Football.")
elif 200 <= result <= 299:
    print(f"Good job! You scored {result} points, and you've won Teddy Bear.")
elif result >= 300:
    print(f"Good job! You scored {result} points, and you've won Lego Construction Set.")
else:
    print(f'Sorry! You need {100 - result} points more to win a prize.')
