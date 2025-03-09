def is_perfect(num):
    temp = num
    for i in range(1, num):
        if num % i == 0:
            temp -= i

    if temp == 0:
        return "We have a perfect num!"
    return "It's not so perfect."


number = int(input())
print(is_perfect(number))