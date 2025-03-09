x = int(input())
y = int(input())

for i in range(x, 0, -1):
    for j in range(y):
        if i == x:
            print(f"L{x}{j}", end=" ")
        elif i%2 == 0:
            print(f"O{i}{j}", end=" ")
        else:
            print(f"A{i}{j}", end=" ")
    print("")
