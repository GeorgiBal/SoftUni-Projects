import sys

n = int(input())
max_num = -sys.maxsize
total = 0

for i in range(n):
    num = int(input())
    if num > max_num:
        max_num = num
    total += num

if total-max_num == max_num:
    print("Yes")
    print("Sum =", total-max_num)
else:
    print("No")
    sum_others = total - max_num
    print("Diff =", abs(max_num - sum_others))