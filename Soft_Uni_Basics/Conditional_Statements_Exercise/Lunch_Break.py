from math import ceil

serial = input()
episode = int(input())
rest = int(input())

lunch = rest/8
relax = rest/4

time = rest - lunch - relax

if time >= episode:
    print(f"You have enough time to watch {serial} and left with {ceil(time-episode)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial}, you need {ceil(episode-time)} more minutes.")