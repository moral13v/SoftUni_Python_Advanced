def numbers_searching(*args):
    numbers = [int(x) for x in args]
    max_missing_value = max(numbers) - 1
    duplicates = []
    uniques = []
    result = []

    for number in numbers:
        if number not in uniques:
            uniques.append(number)
        else:
            if number not in duplicates:
                duplicates.append(number)

    while max_missing_value in numbers:
        max_missing_value -= 1

    result.append(max_missing_value)
    result.append(sorted(duplicates))

    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))

