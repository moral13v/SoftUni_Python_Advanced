text = input()

char_occ = {}

for ch in text:
    if ch not in char_occ:
        char_occ[ch] = 0
    char_occ[ch] += 1

for kvp in sorted(char_occ.items()):
    print(f"{kvp[0]}: {kvp[1]} time/s")
