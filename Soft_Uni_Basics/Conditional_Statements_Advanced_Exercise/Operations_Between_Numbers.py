n1 = int(input())
n2 = int(input())
operator = input()
status = ""

if operator == "+":
    result = n1 + n2
    if result%2 == 0:
        status = "even"
    else:
        status = "odd"
    print(f"{n1} + {n2} = {result} - {status}")
elif operator == "-":
    result = n1 - n2
    if result % 2 == 0:
        status = "even"
    else:
        status = "odd"
    print(f"{n1} - {n2} = {result} - {status}")
elif operator == "*":
    result = n1 * n2
    if result % 2 == 0:
        status = "even"
    else:
        status = "odd"
    print(f"{n1} * {n2} = {result} - {status}")
elif operator == "/":
    if n1 == 0:
        print(f"Cannot divide {n2} by zero")
    elif n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 / n2
        print(f"{n1} / {n2} = {result:.2f}")
elif operator == "%":
    if n1 == 0:
        print(f"Cannot divide {n2} by zero")
    elif n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 % n2
        print(f"{n1} % {n2} = {result}")


