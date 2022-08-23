from statistics import mean

n = int(input())

students = {}

for i in range(n):
    line = tuple(input().split())
    student, grade = line
    if student not in students:
        students[student] = []
    students[student].append(float(grade))

for key, value in students.items():
    # print(f"{key} ->", end=" ")
    # [print(f"{x:.2f}", end=" ") for x in value]
    # print(f"(avg: {(sum(value) / len(value)):.2f})")

    print(f"{key} -> {' '.join([f'{x:.2f}' for x in value])} (avg: {mean(value):.2f})")
