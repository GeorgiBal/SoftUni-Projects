rooms = int(input())
free_space = True
free_chairs = 0


for room in range(rooms):
    chairs, visitors = input().split()
    chairs = len(chairs)
    visitors = int(visitors)

    if visitors <= chairs:
        free_chairs += (chairs - visitors)
    else:
        print(f"{visitors - chairs} more chairs needed in room {room + 1}")
        free_space = False

if free_space:
    print(f"Game On, {free_chairs} free chairs left")