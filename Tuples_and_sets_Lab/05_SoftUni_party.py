n = int(input())

regular = set()
VIP = set()

for i in range(n):
    res_code = input()
    if res_code[0].isnumeric():
        VIP.add(res_code)
    else:
        regular.add(res_code)

arriving_guest = input()

while arriving_guest != "END":
    if arriving_guest in VIP:
        VIP.remove(arriving_guest)
    elif arriving_guest in regular:
        regular.remove(arriving_guest)
    arriving_guest = input()

sorted_VIP = sorted(VIP)
sorted_Regular = sorted(regular)

no_show = len(VIP) + len(regular)
print(no_show)
[print(person) for person in sorted_VIP]
[print(person) for person in sorted_Regular]
