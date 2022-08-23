n = int(input())

max_length = 0
longest_set = None

for _ in range(n):
    set_a = set()
    set_b = set()
    first_range, second_range = input().split("-")
    first_range_start, first_range_end = first_range.split(",")
    second_range_start, second_range_end = second_range.split(",")

    for num in range(int(first_range_start), int(first_range_end) + 1, 1):
        set_a.add(num)
    for num in range(int(second_range_start), int(second_range_end) + 1, 1):
        set_b.add(num)

    if len(set_a.intersection(set_b)) > max_length:
        longest_set = set_a.intersection(set_b)
        max_length = len(longest_set)

print(f"Longest intersection is {list(longest_set)} with length {len(longest_set)}")

