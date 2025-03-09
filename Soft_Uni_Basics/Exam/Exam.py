n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
total = 0
for i in range(n):
    num = float(input())
    total += num
    if 2 <= num <= 2.99:
        p1 += 1
    elif 3 <= num <= 3.99:
        p2 += 1
    elif 4 <= num <= 4.99:
        p3 += 1
    elif 5 <= num:
        p4 += 1

p1 = p1/n*100
p2 = p2/n*100
p3 = p3/n*100
p4 = p4/n*100
print(f"Top students: {p4:.2f}%")
print(f"Between 4.00 and 4.99: {p3:.2f}%")
print(f"Between 3.00 and 3.99: {p2:.2f}%")
print(f"Fail: {p1:.2f}%")
print(f"Average: {total/n:.2f}")
