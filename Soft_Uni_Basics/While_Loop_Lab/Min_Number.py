import sys

num = sys.maxsize
while True:
    text = input()
    if text == "Stop":
        break
    elif int(text) < num:
        num = int(text)

print(num)
