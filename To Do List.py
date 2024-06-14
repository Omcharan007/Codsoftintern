import json
import os

TODO_FILE = 'todo_list.json'

def load_tasks():
    """Load tasks from a JSON file."""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to a JSON file."""
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter a new task: ")
    tasks.append({"task": task, "done": False})
    print(f'Task "{task}" added.')

def view_tasks(tasks):
    """View all tasks in the list."""
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{i}. {task['task']} - {status}")

def mark_task_done(tasks):
    """Mark a specified task as done."""
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the number of the task to mark as done: "))
            if 0 < task_num <= len(tasks):
                tasks[task_num - 1]["done"] = True
                print(f'Task "{tasks[task_num - 1]["task"]}" marked as done.')
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def remove_task(tasks):
    """Remove a specified task from the list."""
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the number of the task to remove: "))
            if 0 < task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f'Task "{removed_task["task"]}" removed.')
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    """Main function to run the to-do list application."""
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as done")
        print("4. Remove task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
