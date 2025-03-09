courses = {}

while True:
    course = input()

    if course == "end":
        break

    course_name, student_name = course.split(" : ")

    if course_name not in courses.keys():
        courses[course_name] = []

    if student_name not in courses[course_name]:
        courses[course_name].append(student_name)

for course, students in courses.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")