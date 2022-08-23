try:
    with open("numbers.txt") as file:
        print(sum([int(line_num) for line_num in file.readlines()]))
except FileNotFoundError:
    print("File was not found")
