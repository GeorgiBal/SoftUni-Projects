num = int(input())
start_points = int(input())
points = start_points
wins = 0
for i in range(num):
    stage = input()
    if stage == "W":
        points += 2000
        wins += 1
    elif stage == "F":
        points += 1200
    elif stage == "SF":
        points += 720

print("Final points:", points)
print(f"Average points: {int((points-start_points)/num)}")
print(f"{wins/num*100:.2f}%")