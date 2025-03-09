n = int(input())
first_sum = 0
second_sum = 0
for i in range(n):
    if i%2:
        num = int(input())
        first_sum += num
    else:
        num = int(input())
        second_sum += num

if first_sum == second_sum:
    print("Yes")
    print("Sum =", first_sum)
else:
    print("No")
    print("Diff =", abs(first_sum-second_sum))