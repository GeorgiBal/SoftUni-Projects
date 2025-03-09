snowballs = int(input())

snowball_weight = 0
snowball_time = 0
snowball_quality = 0

highest = 0

for i in range(snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())

    value = (weight / time) ** quality
    if value > highest:
        highest = value
        snowball_weight = weight
        snowball_time = time
        snowball_quality = quality

print(f"{snowball_weight} : {snowball_time} = {int(highest)} ({snowball_quality})")


