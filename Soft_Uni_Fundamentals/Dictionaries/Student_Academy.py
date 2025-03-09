lines = int(input())
students = {}

for line in range(lines):

    name = input()
    grade = float(input())

    if name not in students.keys():
        students[name] = [grade, 1]
    else:
        students[name][0] += grade
        students[name][1] += 1


for name, grades in students.items():
    average = grades[0]/grades[1]
    if average >= 4.5:
        print(f"{name} -> {average:.2f}")