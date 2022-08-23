from collections import deque


def are_presents_crafted(gift_1, gift_2):
    if gift_1 > 0 and gift_2 > 0:
        return True


presents = {"Doll": 0, "Wooden train": 0, "Teddy bear": 0, "Bicycle": 0}

material_stack = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())

while material_stack and magic:

    if material_stack[-1] == 0 or magic[0] == 0:
        if material_stack[-1] == 0:
            material_stack.pop()
        if magic[0] == 0:
            magic.popleft()
        continue

    current_material = material_stack.pop()
    current_magic = magic.popleft()
    result = current_material * current_magic

    if result == 150:
        presents["Doll"] += 1
    elif result == 250:
        presents["Wooden train"] += 1
    elif result == 300:
        presents["Teddy bear"] += 1
    elif result == 400:
        presents["Bicycle"] += 1
    elif result < 0:
        new_material = current_material + current_magic
        material_stack.append(new_material)
    else:
        new_material = current_material + 15
        material_stack.append(new_material)


if are_presents_crafted(presents["Doll"], presents["Wooden train"]) \
        or are_presents_crafted(presents["Teddy bear"], presents["Bicycle"]):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if material_stack:
    print(f"Materials left: {', '.join([str(x) for x in reversed(material_stack)])}")
if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")

for key, value in sorted(presents.items()):
    if value > 0:
        print(f"{key}: {value}")
