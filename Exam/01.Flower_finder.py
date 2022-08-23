from collections import deque

vowels = deque(input().split())
consonants = input().split()

flowers = {'rose': ['r', 'o', 's', 'e'],
           'tulip': ['t', 'u', 'l', 'i', 'p'],
           'lotus': ['l', 'o', 't', 'u', 's'],
           'daffodil': ['d', 'a', 'f', 'o', 'i', 'l']}

flower_found = False
word = None

while vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()
    for key, value in flowers.items():
        if current_vowel in value:
            value.remove(current_vowel)
            if any(len(value) == 0 for value in flowers.values()):
                word = key
                flower_found = True
                break
        if current_consonant in value:
            value.remove(current_consonant)
            if any(len(value) == 0 for value in flowers.values()):
                word = key
                flower_found = True
                break
    if flower_found:
        break


if flower_found:
    print(f"Word found: {word}")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")

