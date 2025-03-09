length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = (length*width*height)/1000
litres = volume*(1 - (percent/100))
print(litres)