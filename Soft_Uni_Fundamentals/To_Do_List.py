to_do_list = []


def add_task(task):
    to_do_list.append(task)
    print("Task added successfully")


def remove_task(task):
    if task in to_do_list:
        to_do_list.remove(task)
        print("Task removed successfully")
    else:
        print("Task not found in the list")


def view_tasks():
    if to_do_list:
        print("Tasks:")
        for task in to_do_list:
            print(task)
    else:
        print("No tasks in the To Do List")


while True:
    print("\n --- To Do List App ---")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Enter your choice(1-4): ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter task to remove: ")
        remove_task(task)
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        print("Exiting the program!")
        break
    else:
        print("Invalid choice, please try again")