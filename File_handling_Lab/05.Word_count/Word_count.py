import re

searched_words = []

with open("words.txt") as file:
    searched_words = file.read().split()

words_count = {}

with open("input.txt") as file:
    text = file.read()
    for word in searched_words:
        pattern = fr"\b{word}\b"
        count = len(re.findall(pattern, text, re.IGNORECASE))
        words_count[word] = count

with open("output.txt", "w") as file:
    sorted_result = sorted(words_count.items(), key=lambda kvpt: -kvpt[1])
    for key, value in sorted_result:
        file.writelines(f"{key} - {value}\n")
