words = input().split()
total_sum = 0

for word in words:
    num = int(word[1: -1])

    if word[0].isupper():
        num /= ord(word[0]) - 64
    elif word[0].islower():
        num *= ord(word[0]) - 96

    total_sum += num

    if word[-1].isupper():
        total_sum -= ord(word[-1]) - 64
    elif word[-1].islower():
        total_sum += ord(word[-1]) - 96


print(f"{total_sum:.2f}")
