import sys

n = int(input())
max_num = -sys.maxsize
min_num = sys.maxsize
for i in range(n):
    num = int(input())
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num


print("Max number:", max_num)
print("Min number:", min_num)
