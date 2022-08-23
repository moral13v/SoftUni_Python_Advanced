from collections import deque

name = input()
line = deque()

while name != "End":
    if name == "Paid":
        # for name in line:
        #     print(name)
        # line.clear()
        while line:
            print(line.popleft())
        # name = input()
        # continue
    else:
        line.append(name)
    name = input()

print(f"{len(line)} people remaining.")


