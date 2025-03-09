n = int(input())
count = 0
counter = 0

while True:
    presentation = input()
    if presentation == "Finish":
        print(f"Student's final assessment is {count/counter:.2f}.")
        break

    total = 0
    for i in range(n):
        grade = float(input())
        total += grade
        counter += 1

    print(f"{presentation} - {total/n:.2f}.")
    count += total