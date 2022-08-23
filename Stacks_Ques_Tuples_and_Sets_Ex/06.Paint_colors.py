from collections import deque

main_colors = ['red', 'yellow', 'blue']
sec_colors = ['orange', 'purple', 'green']
found_colors = []

line = deque(input().split())

while line:
    first_sub = line.popleft()
    second_sub = line.pop() if line else ''

    result = first_sub + second_sub
    if result in main_colors or result in sec_colors:
        found_colors.append(result)
        continue

    result = second_sub + first_sub
    if result in main_colors or result in sec_colors:
        found_colors.append(result)
        continue

    first_sub = first_sub[:-1]
    second_sub = second_sub[:-1]

    if first_sub:
        line.insert(len(line) // 2, first_sub)
    if second_sub:
        line.insert(len(line) // 2, second_sub)

result = []
required_colors = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue']
}

for color in found_colors:
    if color in main_colors:
        result.append(color)
    else:
        is_valid = True
        for required_color in required_colors[color]:
            if required_color not in found_colors:
                is_valid = False
                break
        if is_valid:
            result.append(color)

print(result)

