exam_h = int(input())
exam_m = int(input())
arrive_h = int(input())
arrive_m = int(input())
status = ""

exam_all_min = (exam_h*60) + exam_m
arr_all_min = (arrive_h*60) + arrive_m

if arr_all_min > exam_all_min:
    status = "Late"
    print("Late")
elif exam_all_min == arr_all_min or exam_all_min - arr_all_min <= 30:
    status = "On time"
    print("On time")
else:
    status = "Early"
    print("Early")

time = exam_all_min - arr_all_min
if time != 0:
    if status == "Early" or status == "On time":
        if time < 60:
            print(f"{time} minutes before the start")
        else:
            hour = time//60
            minutes = time-(hour*60)
            if minutes < 10:
                print(f"{hour}:0{minutes} hours before the start")
            else:
                print(f"{hour}:{minutes} hours before the start")

    if status == "Late":
        time = arr_all_min - exam_all_min
        if time < 60:
            print(f"{time} minutes after the start")
        else:
            hour = time//60
            minutes = time-(hour*60)
            if minutes < 10:
                print(f"{hour}:0{minutes} hours after the start")
            else:
                print(f"{hour}:{minutes} hours after the start")

