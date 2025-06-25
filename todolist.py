class TodoList:
    def __init__(self):
        self.tasks = []

    def show_menu(self):
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                status = "Done" if task['completed'] else "Pending"
                print(f"{i}. {task['title']} [{status}]")

    def add_task(self):
        title = input("Enter task name: ")
        task = {"title": title, "completed": False}
        self.tasks.append(task)
        print("Task added.")

    def complete_task(self):
        self.view_tasks()
        if self.tasks:
            try:
                num = int(input("Enter task number to mark as completed: "))
                if 1 <= num <= len(self.tasks):
                    self.tasks[num - 1]["completed"] = True
                    print("Task marked as completed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    def delete_task(self):
        self.view_tasks()
        if self.tasks:
            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(self.tasks):
                    removed = self.tasks.pop(num - 1)
                    print(f"Task '{removed['title']}' deleted.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Choose an option: ")

            if choice == '1':
                self.view_tasks()
            elif choice == '2':
                self.add_task()
            elif choice == '3':
                self.complete_task()
            elif choice == '4':
                self.delete_task()
            elif choice == '5':
                print("Exiting To-Do List. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Main Program
if __name__ == "__main__":
    todo = TodoList()
    todo.run()
