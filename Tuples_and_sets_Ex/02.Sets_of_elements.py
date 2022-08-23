n, m = input().split()

set_a = set()
set_b = set()

for i in range(int(n)):
    num = int(input())
    set_a.add(num)

for i in range(int(m)):
    num = int(input())
    set_b.add(num)

for el in set_a.intersection(set_b):
    print(el)
