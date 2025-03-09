s = int(input())
e = int(input())
num = int(input())
combination = 0
num_com = 0

for i in range(s, e+1):
    for j in range(s, e+1):
        combination += 1
        if i + j == num:
            num_com = combination
            print(f"Combination N:{num_com} ({i} + {j} = {num})")
            break
    if num_com == combination:
        break

if num_com != combination:
    print(f"{combination} combinations - neither equals {num}")