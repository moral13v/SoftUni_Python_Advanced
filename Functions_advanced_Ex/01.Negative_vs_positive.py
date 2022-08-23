line = input().split()

sum_negative = sum([int(x) for x in line if int(x) < 0])
sum_positive = sum([int(x) for x in line if int(x) > 0])

# sum_negative = 0
# sum_positive = 0
# 
# for num in line:
#     if int(num) < 0:
#         sum_negative += int(num)
#     else:
#         sum_positive += int(num)

print(sum_negative)
print(sum_positive)
if abs(sum_negative) > sum_positive:
    print("The negatives are stronger than the positives")
elif abs(sum_negative) < sum_positive:
    print("The positives are stronger than the negatives")
