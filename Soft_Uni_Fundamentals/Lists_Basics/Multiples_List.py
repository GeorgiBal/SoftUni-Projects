factor = int(input())
count = int(input())

ls = []
num = factor
while len(ls) != count:
    ls.append(num)
    num += factor

print(ls)
