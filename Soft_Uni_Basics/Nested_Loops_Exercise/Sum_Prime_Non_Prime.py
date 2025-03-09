prime = 0
non_prime = 0
num = input()
while num != "stop":

    num = int(num)
    count = 0

    if num < 0:
        print("Number is negative.")
        num = input()
        continue

    for i in range(1, num+1):
        if num % i == 0:
            count += 1

    if count == 2:
        prime += num
    else:
        non_prime += num

    num = input()


print(f"Sum of all prime numbers is: {prime}")
print(f"Sum of all non prime numbers is: {non_prime}")
