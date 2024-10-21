def display_todo_list(todo_list):
    print("\nTo-Do List:")
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        for idx, task in enumerate(todo_list, start=1):
            print(f"{idx}. {task}")
    print()

def main():
    todo_list = []
    
    while True:
        print("Options:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            task = input("Enter a new task: ")
            todo_list.append(task)
            print(f"Added task: '{task}'")
        
        elif choice == '2':
            display_todo_list(todo_list)
        
        elif choice == '3':
            display_todo_list(todo_list)
            try:
                task_num = int(input("Enter the task number to remove: "))
                if 1 <= task_num <= len(todo_list):
                    removed_task = todo_list.pop(task_num - 1)
                    print(f"Removed task: '{removed_task}'")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == '4':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
