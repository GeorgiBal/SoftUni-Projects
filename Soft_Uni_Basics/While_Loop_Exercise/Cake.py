w = int(input())
l = int(input())
size = w*l

while True:
    pieces = input()
    if pieces == "STOP":
        print(f"{size} pieces are left.")
        break
    else:
        size -= int(pieces)
        if size < 0:
            print(f"No more cake left! You need {-size} pieces more.")
            break
