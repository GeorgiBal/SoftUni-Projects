nation = input()
device = input()
points = 0

if nation == "Bulgaria":
    if device == "ribbon":
        points = 9.6 + 9.4
    elif device == "hoop":
        points = 9.55 + 9.75
    elif device == "rope":
        points = 9.5 + 9.4
elif nation == "Russia":
    if device == "ribbon":
        points = 9.1 + 9.4
    elif device == "hoop":
        points = 9.3 + 9.8
    elif device == "rope":
        points = 9.6 + 9
elif nation == "Italy":
    if device == "ribbon":
        points = 9.2 + 9.5
    elif device == "hoop":
        points = 9.45 + 9.35
    elif device == "rope":
        points = 9.7 + 9.15


points_needed = 20 - points
print(f"The team of {nation} get {points:.3f} on {device}.")
print(f"{(points_needed/20)*100:.2f}%")