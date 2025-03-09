n = int(input())
condition = False

for a in range(1, 9):
    if condition:
        break
    for b in range(9, a, -1):
        if condition:
            break
        for c in range(0, 9):
            if condition:
                break
            for d in range(9, c, -1):
                if condition:
                    break
                if a + b + c + d == a * b * c * d and n % 10 == 5:
                    print(str(a) + str(b) + str(c) + str(d))
                    condition = True
                    break
                elif int((a * b * c * d)/(a + b + c + d)) == 3 and n % 3 == 0:
                    print(str(d) + str(c) + str(b) + str(a))
                    condition = True
                    break

if not condition:
    print("Nothing found")
