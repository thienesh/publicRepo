import os

TODO_FILE = "todo.txt"


def display_menu():
    print("To-Do List Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")


def add_task():
    task_description = input("Enter task description: ")
    with open(TODO_FILE, "a") as file:
        file.write(f"{task_description}\n")
    print("Task added successfully!")


def view_tasks():
    with open(TODO_FILE, "r") as file:
        tasks = file.readlines()
        if tasks:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
        else:
            print("No tasks found.")


def mark_task_completed():
    tasks = read_tasks()
    if tasks:
        view_tasks()
        task_index = get_task_index(tasks)
        if task_index is not None:
            tasks[task_index] = tasks[task_index].replace("[ ]", "[x]")
            write_tasks(tasks)
            print("Task marked as completed.")
    else:
        print("No tasks found.")


def delete_task():
    tasks = read_tasks()
    if tasks:
        view_tasks()
        task_index = get_task_index(tasks)
        if task_index is not None:
            deleted_task = tasks.pop(task_index)
            write_tasks(tasks)
            print(f"Task '{deleted_task.strip()}' deleted.")
    else:
        print("No tasks found.")


def read_tasks():
    with open(TODO_FILE, "r") as file:
        return file.readlines()


def write_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        file.writelines(tasks)


def get_task_index(tasks):
    while True:
        try:
            task_index = int(input("Enter task number: ")) - 1
            if 0 <= task_index < len(tasks):
                return task_index
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

    print("Goodbye!")


if __name__ == "__main__":
    if not os.path.isfile(TODO_FILE):
        open(TODO_FILE, "w").close()
    main()
