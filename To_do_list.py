class ToDoList:
    def __init__1(self):
        self.tasks = []

    def add_task(self):
        task = input("Enter task: ")
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def remove_task(self):
        if not self.tasks:
            print("No tasks to remove.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks):
                print(f"{i+1}. {task}")
            task_number = int(input("Enter task number to remove: ")) - 1
            if task_number < 0 or task_number >= len(self.tasks):
                print("Invalid task number.")
            else:
                task = self.tasks.pop(task_number)
                print(f"Task '{task}' removed.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks):
                print(f"{i+1}. {task}")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            todo_list.add_task()
        elif choice == "2":
            todo_list.remove_task()
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            print("Exiting To-Do List app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()