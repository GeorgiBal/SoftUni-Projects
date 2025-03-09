bad_grades = int(input())
count = 0
grades = 0
poor_grades = 0
problem = ""

while True:
    task = input()

    if task == "Enough":
        print(f"Average score: {grades/count:.2f}")
        print(f"Number of problems: {count}")
        print(f"Last problem: {problem}")
        break
    else:
        grade = int(input())
        grades += grade
        count += 1
        problem = task
        if grade <= 4:
            poor_grades += 1

    if poor_grades == bad_grades:
        print(f"You need a break, {bad_grades} poor grades.")
        break
