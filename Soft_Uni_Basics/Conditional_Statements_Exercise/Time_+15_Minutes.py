hour = int(input())
minutes = int(input())
added_time = minutes + 15

if added_time == 60:
    hour += 1
    if hour == 24:
        hour = 0
    print(f"{hour}:00")
elif added_time > 60 and added_time - 60 >= 10:
    hour += 1
    if hour == 24:
        hour = 0
    print(f"{hour}:{added_time-60}")
elif added_time > 60 and added_time - 60 < 10:
    hour += 1
    if hour == 24:
        hour = 0
    print(f"{hour}:0{added_time-60}")
else:
    print(f"{hour}:{added_time}")
