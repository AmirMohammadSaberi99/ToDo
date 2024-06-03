import os

class ToDoList:
    def __init__(self, filename="todo_list.txt"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                tasks = [line.strip() for line in file.readlines()]
        else:
            tasks = []
        return tasks

    def save_tasks(self):
        with open(self.filename, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
        print(f"Added task: {task}")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            self.save_tasks()
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task number")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def main(self):
        while True:
            print("\nTo-Do List Application")
            print("1. View To-Do List")
            print("2. Add Task")
            print("3. Remove Task")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.display_tasks()
            elif choice == '2':
                task = input("Enter the task: ")
                self.add_task(task)
            elif choice == '3':
                self.display_tasks()
                try:
                    index = int(input("Enter the task number to remove: ")) - 1
                    self.remove_task(index)
                except ValueError:
                    print("Invalid input. Please enter a number.")
            elif choice == '4':
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.main()
