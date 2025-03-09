n = int(input())
tank = 255

for i in range(n):
    l = int(input())
    if tank - l < 0:
        print("Insufficient capacity!")
        continue
    tank -= l

print(255 - tank)
