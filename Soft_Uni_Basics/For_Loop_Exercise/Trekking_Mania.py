groups = int(input())
total = 0
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for i in range(groups):
    people = int(input())
    total += people
    if people <= 5:
        p1 += people
    elif 6 <= people <= 12:
        p2 += people
    elif 13 <= people <= 25:
        p3 += people
    elif 26 <= people <= 40:
        p4 += people
    elif people >= 41:
        p5 += people

print(f"{p1/total*100:.2f}%")
print(f"{p2/total*100:.2f}%")
print(f"{p3/total*100:.2f}%")
print(f"{p4/total*100:.2f}%")
print(f"{p5/total*100:.2f}%")
