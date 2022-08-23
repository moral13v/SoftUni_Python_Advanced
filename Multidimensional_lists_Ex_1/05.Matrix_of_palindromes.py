rows, cols = [int(x) for x in input().split()]

matrix = []

for row in range(rows):
    line = []
    for col in range(cols):
        el = f"{chr(97 + row)}{chr(97 + row + col)}{chr(97 + row)}"
        line.append(el)
    matrix.append(line)

for row in matrix:
    print(" ".join(row))
