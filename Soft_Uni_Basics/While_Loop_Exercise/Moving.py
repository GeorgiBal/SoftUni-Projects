w = int(input())
l = int(input())
h = int(input())
space = w*l*h

while True:
    boxes = input()
    if boxes == "Done":
        print(f"{space} Cubic meters left.")
        break
    else:
        space -= int(boxes)
        if space < 0:
            print(f"No more free space! You need {-space} Cubic meters more.")
            break