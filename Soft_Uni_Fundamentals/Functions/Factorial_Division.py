def factorial(number):
    for i in range(1, number):
        number *= i

    return number


num1 = int(input())
num2 = int(input())
num1_fact = factorial(num1)
num2_fact = factorial(num2)
result = num1_fact/num2_fact
print(f"{result:.2f}")
