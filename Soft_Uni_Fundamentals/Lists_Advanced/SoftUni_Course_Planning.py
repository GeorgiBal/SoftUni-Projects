def add_lesson(list_lessons, lesson_title):
    if lesson_title not in list_lessons:
        list_lessons.append(lesson_title)
    return list_lessons


def insert_lesson(list_lessons, lesson_title, index):
    if lesson_title not in list_lessons:
        list_lessons.insert(int(index), lesson_title)
    return list_lessons


def remove_lesson(list_lessons, lesson_title):
    if lesson_title in list_lessons:
        list_lessons.remove(lesson_title)
        if f"{lesson_title}-Exercise" in list_lessons:
            list_lessons.remove(f"{lesson_title}-Exercise")
    return list_lessons


def swap_lesson(list_lessons, lesson1, lesson2):
    if lesson1 in list_lessons and lesson2 in list_lessons:
        index1 = list_lessons.index(lesson1)
        index2 = list_lessons.index(lesson2)
        index1_ex = f"{list_lessons[index1]}-Exercise" in list_lessons
        index2_ex = f"{list_lessons[index2]}-Exercise" in list_lessons

        list_lessons[index1], list_lessons[index2] = list_lessons[index2], list_lessons[index1]

        if index1_ex and index2_ex:
            list_lessons[index1 + 1], list_lessons[index2 + 1] = list_lessons[index2 + 1], list_lessons[index1 + 1]
        elif not index1_ex and index2_ex:
            list_lessons.insert(index1 + 1, list_lessons.pop(index2 + 1))
        elif index1_ex and not index2_ex:
            list_lessons.insert(index2 + 1, list_lessons.pop(index1 + 1))
    return list_lessons


def exercise(list_lessons, lesson_title):
    if lesson_title in list_lessons and f"{lesson_title}-Exercise" not in list_lessons:
        title_index = list_lessons.index(lesson_title)
        list_lessons.insert(title_index + 1, f"{lesson_title}-Exercise")
    elif lesson_title not in list_lessons:
        list_lessons.append(lesson_title)
        list_lessons.append(f"{lesson_title}-Exercise")
    return list_lessons


lessons = input().split(", ")

while True:
    command = input()
    if command == "course start":
        break
    else:
        command = command.split(":")
        action = command[0]
        lesson = command[1]

        if len(command) > 2:
            index_lesson = command[2]

        if action == "Add":
            lessons = add_lesson(lessons, lesson)

        elif action == "Insert":
            lessons = insert_lesson(lessons, lesson, index_lesson)

        elif action == "Remove":
            lessons = remove_lesson(lessons, lesson)

        elif action == "Swap":
            lessons = swap_lesson(lessons, lesson, index_lesson)

        elif action == "Exercise":
            lessons = exercise(lessons, lesson)


for index, name in enumerate(lessons):
    print(f"{index+1}.{name}")

