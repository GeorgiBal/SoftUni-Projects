record = float(input())
distance = float(input())
seconds = float(input())

time = distance*seconds
water = int((distance/15))*12.5

total_time = time + water

if total_time >= record:
    print("No, he failed! He was {:.2f} seconds slower.".format(total_time-record))
else:
    print("Yes, he succeeded! The new world record is {:.2f} seconds.".format(total_time))