name = input()
points = float(input())
n = int(input())

for i in range(n):
    g_name = input()
    g_points = float(input())
    points += (len(g_name)*g_points)/2
    if points > 1250.5:
        break

if points > 1250.5:
    print(f"Congratulations, {name} got a nominee for leading role with {points:.1f}!")
else:
    print(f"Sorry, {name} you need {1250.5-points:.1f} more!")