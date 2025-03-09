n = int(input())
num = 1
flag = False

for row in range(1, n+1):
    for col in range(1, row+1):

        if num > n:
            flag = True
            break

        print(num, end=" ")
        num += 1
    if flag:
        break
    print()


