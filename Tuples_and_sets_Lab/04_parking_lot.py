n = int(input())

parking = set()

for i in range(n):
    command, reg = input().split(", ")
    if command == "IN":
        parking.add(reg)
    elif command == "OUT" and reg in parking:
        parking.remove(reg)

if not parking:
    print("Parking Lot is Empty")
else:
    for car in parking:
        print(car)
