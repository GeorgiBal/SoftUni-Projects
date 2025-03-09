name = input()
grade = 0
count = 0
excluded = 0

while True:
    grades = float(input())
    grade += 1

    if grades < 4:
        excluded += 1
        if excluded == 2:
            print(f"{name} has been excluded at {grade} grade")
            break
        grade -= 1
    else:
        count += grades
    if grade == 12:
        print(f"{name} graduated. Average grade: {(count / grade):.2f}")
        break


