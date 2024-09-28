
menu_list = {
    "1": "1. View Tasks",
    "2": "2. Add Task",
    "3": "3. Remove Task",
    "4": "4. Exit",
}

tasks = []


def display_menu(menu):
    while True:
        print("Todo List Menu:")
        for item in menu:
            print(f"{menu[item]}")
        try:
            choice = input("Enter your choice: ")
            if not menu_list[str(choice)]:
                raise KeyError
            return choice
        except KeyError:
            print("Please enter a valid choice\n")
            continue

def add_task(tasks):
    name = input("Enter a new Task: ")
    tasks.append({
        'name': name,
        "id": tasks[len(tasks) - 1] + 1 if len(tasks) > 0 else 1
    })

def view_tasks(tasks):
    print("List of Tasks:")
    if len(tasks) == 0:
        print("Empty list!\n")
    else:
        for task in tasks:
            print(f"{task["id"]}. {task["name"]}")

def remove_task(tasks):
    if len(tasks) == 0:
        return print("List if empty")
    while True:
        try:
            task_id = int(input("Enter task ID: "))
            task = next((task for task in tasks if task["id"] == task_id), None)
            if task == None:
                raise ValueError
            else:
                # tasks = list(filter(lambda task: task["id"] != task_id, tasks))
                tasks.remove(task)
                break
        except ValueError:
            print("Invalid task ID")
            continue

def main():
    while True:
        cases = {
            "1": view_tasks,
            "2": add_task,
            "3": remove_task,
            "4": None
        }

        choice = display_menu(menu_list)
        if choice == "4":
            break

        if choice in cases and cases[choice]:
            cases[choice](tasks)
            continue


if __name__ == "__main__":
    main()
