n = int(input())
total = 0

for i in range(n):
    char = input()
    num = ord(char)
    total += num

print(f"The sum equals: {total}")

