from collections import deque

bomb_effects = deque(int(x) for x in input().split(', '))
bomb_casings = [int(x) for x in input().split(', ')]

bombs = {40: 'Datura Bombs',
         60: 'Cherry Bombs',
         120: 'Smoke Decoy Bombs'}

inventory = {'Datura Bombs': 0,
         'Cherry Bombs': 0,
         'Smoke Decoy Bombs': 0}

full_pouch = False

while bomb_effects and bomb_casings:
    bomb = bomb_effects[0] + bomb_casings[-1]
    if bomb in bombs.keys():
        inventory[bombs[bomb]] += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    else:
        bomb_casings[-1] -= 5

    if all(value >= 3 for value in inventory.values()):
        full_pouch = True
        break

if full_pouch:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
else:
    print("Bomb Effects: empty")

if bomb_casings:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casings])}")
else:
    print("Bomb Casings: empty")

for key, value in sorted(inventory.items()):
    print(f"{key}: {value}")



