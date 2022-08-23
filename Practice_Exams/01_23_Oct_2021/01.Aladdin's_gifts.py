from collections import deque

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())
presents = {}

while materials and magic:
    result = magic[0] + materials[-1]

    if result < 100:
        if result % 2 == 0:
            result = (materials[-1] * 2) + (magic[0] * 3)
        else:
            result *= 2
    elif result > 499:
        result /= 2

    if 100 <= result <= 199:
        present = "Gemstone"
        if present not in presents:
            presents[present] = 0
        presents[present] += 1
    elif 200 <= result <= 299:
        present = "Porcelain Sculpture"
        if present not in presents:
            presents[present] = 0
        presents[present] += 1
    elif 300 <= result <= 399:
        present = "Gold"
        if present not in presents:
            presents[present] = 0
        presents[present] += 1
    elif 400 <= result <= 499:
        present = "Diamond Jewellery"
        if present not in presents:
            presents[present] = 0
        presents[present] += 1
    else:
        magic.popleft()
        materials.pop()
        continue

    magic.popleft()
    materials.pop()

if "Gemstone" in presents.keys() and "Porcelain Sculpture" in presents.keys() or\
        "Gold" in presents.keys() and "Diamond Jewellery" in presents.keys():
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")

for present, quantity in sorted(presents.items()):
    print(f"{present}: {quantity}")
