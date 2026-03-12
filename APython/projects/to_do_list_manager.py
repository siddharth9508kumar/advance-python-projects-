class to_do_list_manager:
    def __init__(self):
        self.to_do_list = []

    def add_task(self, task):
        self.to_do_list.append(task)
        print(f'Task "{task}" added to the to-do list.')

    def remove_task(self, task):
        if task in self.to_do_list:
            self.to_do_list.remove(task)
            print(f'Task "{task}" removed from the to-do list.')
        else:
            print(f'Task "{task}" not found in the to-do list.')
    def set_deadline(self, task, deadline):
        if task in self.to_do_list:
            print(f'Task "{task}" has a deadline set for {deadline}.')
        else:
            print(f'Task "{task}" not found in the to-do list. Cannot set deadline.')
    def assign_priority(self, task, priority):
        if task in self.to_do_list:
            print(f'Task "{task}" has been assigned a priority of {priority}.')
        else:
            print(f'Task "{task}" not found in the to-do list. Cannot assign priority.')
    def mark_task_as_completed(self, task):
        if task in self.to_do_list:
            print(f'Task "{task}" marked as completed.')
        else:
            print(f'Task "{task}" not found in the to-do list. Cannot mark as completed.')
        
    def filter_tasks_by_project(self, project_name):
        print(f'Filtering tasks by project: {project_name}')
    def dashboard(self):
        if not self.to_do_list:
            print("The to-do list is empty.")
        else:
            print("To-Do List:")
            for idx, task in enumerate(self.to_do_list, start=1):
                print(f"{idx}. {task}")


to_do_manager = to_do_list_manager()

while True:
    print("\nTo-Do List Manager")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Set Deadline")
    print("4. Assign Priority")
    print("5. Mark Task as Completed")
    print("6. Filter Tasks by Project")
    print("7. View Dashboard")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task to add: ")
        to_do_manager.add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove: ")
        to_do_manager.remove_task(task)
    elif choice == '3':
        task = input("Enter the task to set a deadline for: ")
        deadline = input("Enter the deadline (e.g., YYYY-MM-DD): ")
        to_do_manager.set_deadline(task, deadline)
    elif choice == '4':
        task = input("Enter the task to assign a priority to: ")
        priority = input("Enter the priority (e.g., High, Medium, Low): ")
        to_do_manager.assign_priority(task, priority)
    elif choice == '5':
        task = input("Enter the task to mark as completed: ")
        to_do_manager.mark_task_as_completed(task)
    elif choice == '6':
        project_name = input("Enter the project name to filter tasks by: ")
        to_do_manager.filter_tasks_by_project(project_name)
    elif choice == '7':
        to_do_manager.dashboard()
    elif choice == '8':
        print("Exiting To-Do List Manager.")
        break
    else:
        print("Invalid choice. Please try again.")
