n = int(input())
first_sum = 0
second_sum = 0
for i in range(n*2):
    if i < n:
        num = int(input())
        first_sum += num
    else:
        num = int(input())
        second_sum += num

if first_sum == second_sum:
    print("Yes, sum =", first_sum)
else:
    print("No, diff =", abs(first_sum-second_sum))