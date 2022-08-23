import string

letter_count = 0
mark_count = 0

with open("text.txt") as file, open("output.txt", "w") as output:

    for row, line in enumerate(file):
        for ch in line:
            if ch in string.punctuation:
                mark_count += 1
            elif ch in string.ascii_letters:
                letter_count += 1

        output.write(f"Line {row + 1}: {line.strip()} ({letter_count})({mark_count})\n")

        letter_count = 0
        mark_count = 0
        