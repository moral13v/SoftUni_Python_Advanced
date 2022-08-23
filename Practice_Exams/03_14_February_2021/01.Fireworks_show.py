from collections import deque

fireworks_effects = deque(int(x) for x in input().split(", ") if int(x) > 0)
explosive_power = [int(x) for x in input().split(", ") if int(x) > 0]

fireworks = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0
}

ready_for_show = False

while fireworks_effects and explosive_power:

    firework = fireworks_effects[0] + explosive_power[-1]

    if firework % 5 == 0 and firework % 3 == 0:
        fireworks["Crossette Fireworks"] += 1
        fireworks_effects.popleft()
        explosive_power.pop()
    elif firework % 3 == 0:
        fireworks["Palm Fireworks"] += 1
        fireworks_effects.popleft()
        explosive_power.pop()
    elif firework % 5 == 0:
        fireworks["Willow Fireworks"] += 1
        fireworks_effects.popleft()
        explosive_power.pop()
    else:
        if fireworks_effects[0] - 1 > 0:
            fireworks_effects.append(fireworks_effects[0] - 1)
        fireworks_effects.popleft()

    if fireworks["Palm Fireworks"] >= 3 and fireworks["Willow Fireworks"] >= 3 and fireworks["Crossette Fireworks"] >= 3:
        ready_for_show = True
        break

if ready_for_show:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks_effects:
    print(f"Firework Effects left: {', '.join([str(x) for x in fireworks_effects])}")
if explosive_power:
    print(f"Explosive Power left: {', '.join([str(x) for x in explosive_power])}")

for key, value in fireworks.items():
    print(f"{key}: {value}")
