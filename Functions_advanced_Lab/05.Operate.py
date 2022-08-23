def operate(operator, *args):
    result = 0
    if operator == '+':
        for num in args:
            result += num
    elif operator == '-':
        for num in args:
            result -= num
    elif operator == '*':
        result = 1
        for num in args:
            result *= num
    elif operator == '/':
        result = 1
        for num in args:
            result /= num
    return result


a = 5
print(operate("/", 3, 4))