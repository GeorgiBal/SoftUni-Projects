from math import pi

figure = input()
if figure == "square":
    num = float(input())
    print(round(num*num, 3))
elif figure == "rectangle":
    num1 = float(input())
    num2 = float(input())
    print(round(num1*num2, 3))
elif figure == "circle":
    num = float(input())
    print(round(pi*num*num, 3))
elif figure == "triangle":
    num1 = float(input())
    num2 = float(input())
    print(round(num1 * num2 / 2, 3))
