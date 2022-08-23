command = input()

line = [int(x) for x in input().split()]

result = 0

if command == "Odd":
    odd_sum = sum(filter(lambda x: x % 2 != 0, line))
    result = odd_sum * len(line)
elif command == "Even":
    even_sum = sum(filter(lambda x: x % 2 == 0, line))
    result = even_sum * len(line)

print(result)
