n = int(input())

odd_set = set()
even_set = set()

for i in range(n):
    name = input()
    ch_sum = 0
    for ch in name:
        ch_sum += ord(ch)
    name_res = ch_sum // (i + 1)
    if name_res % 2 == 0:
        even_set.add(name_res)
    else:
        odd_set.add(name_res)

if sum(odd_set) == sum(even_set):
    print(", ".join([str(x) for x in odd_set.union(even_set)]))
elif sum(odd_set) > sum(even_set):
    print(", ".join([str(x) for x in odd_set.difference(even_set)]))
elif sum(odd_set) < sum(even_set):
    print(", ".join([str(x) for x in odd_set.symmetric_difference(even_set)]))
