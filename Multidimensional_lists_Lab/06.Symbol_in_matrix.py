n = int(input())
data = [input() for _ in range(n)]
symbol = input()
location = ()

is_found = False

for i in range(len(data)):
    if symbol in data[i]:
        is_found = True
        location = (i, data[i].index(symbol))
        break

if is_found:
    print(location)
else:
    print(f"{symbol} does not occur in the matrix")
