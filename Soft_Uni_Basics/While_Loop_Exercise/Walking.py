steps = 0
while True:
    walk = input()
    if walk == "Going home":
        walk = int(input())
        steps += walk
        if steps >= 10000:
            print("Goal reached! Good job!")
            print(f"{steps - 10000} steps over the goal!")
            break
        elif steps < 10000:
            print(f"{10000-steps} more steps to reach goal.")
            break

    steps += int(walk)

    if steps >= 10000:
        print("Goal reached! Good job!")
        print(f"{steps-10000} steps over the goal!")
        break
