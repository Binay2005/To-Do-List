import csv  # Import CSV module to read/write CSV files

# ------------------- Function to Add Task -------------------
def add_task():
    # Get task from user and remove extra spaces
    task_title = input("Enter task description: ").strip()
    if not task_title:
        print("Task cannot be empty.")  # Prevent empty task
        return

    # Open CSV file in append mode to add new task
    with open("to_do_list.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([task_title.capitalize(), " Pending"])  # Add task with initial status


# ------------------- Function to View Tasks -------------------
def view_tasks():
    try:
        # Open CSV file in read mode
        with open("to_do_list.csv", "r") as file:
            reader = csv.reader(file)
            tasks = list(reader)  # Convert CSV rows into a list

            if not tasks:  # Check if file is empty
                print("No tasks found.")
                return

            # Print all tasks with numbering
            print("\nTo-Do List:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. Task: {task[0]} | Status: {task[1]}")

    except FileNotFoundError:  # Handle missing CSV file
        print("No task file found. Please add a task first.")


# ------------------- Function to Delete Task -------------------
def delete_task():
    try:
        # Read all tasks from CSV
        with open("to_do_list.csv", "r") as file:
            reader = csv.reader(file)
            tasks = list(reader)

        if not tasks:
            print("No tasks to delete.")
            return

        # Show tasks to user
        print("\nExisting Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task[0]} | {task[1]}")

        # Ask which task to delete
        task_num = int(input("\nEnter the task number to delete: "))

        # Validate task number
        if task_num < 1 or task_num > len(tasks):
            print("Invalid task number.")
            return

        # Remove task from list
        deleted_task = tasks.pop(task_num - 1)

        # Save updated tasks back to CSV
        with open("to_do_list.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(tasks)

        print(f"Deleted task: {deleted_task[0]}")  # Confirm deletion

    except FileNotFoundError:
        print("Task file not found.")
    except ValueError:
        print("Invalid task number.")


# ------------------- Function to Mark Task as Completed -------------------
def mark_task_done():
    try:
        # Read all tasks from CSV
        with open("to_do_list.csv", "r") as file:
            reader = csv.reader(file)
            tasks = list(reader)

        if not tasks:
            print("No tasks to mark as completed.")
            return

        # Show all tasks
        print("\nExisting Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task[0]} | {task[1]}")

        # Ask which task to mark as completed
        task_num = int(input("\nEnter the task number to mark as completed: "))

        # Validate task number
        if task_num < 1 or task_num > len(tasks):
            print("Invalid task number.")
            return

        # Update status to Completed
        tasks[task_num - 1][1] = " Completed"

        # Save updated tasks back to CSV
        with open("to_do_list.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(tasks)

        print(f"Task marked as completed: {tasks[task_num - 1][0]}")  # Confirm update

    except FileNotFoundError:
        print("Task file not found.")
    except ValueError:
        print("Please enter a valid number.")


# ------------------- Main Program Loop -------------------
print("Welcome to the To-Do List")  

while True:
    # Display menu options
    print("\nPlease select an option:")
    print("1. Add a Task\n2. Remove a Task\n3. View Tasks\n4. Mark Task as Complete\n5. Exit")
    choice = input("Enter your choice (1-5): ")

    # Call function based on user choice
    if choice == "1":
        add_task()
        input("\nPress Enter to continue...")  # Pause for user
    elif choice == "2":
        delete_task()
        input("\nPress Enter to continue...")
    elif choice == "3":
        view_tasks()
        input("\nPress Enter to continue...")
    elif choice == "4":
        mark_task_done()
        input("\nPress Enter to continue...")
    elif choice == "5":
        print("Exiting application.")  # Exit program
        break
    else:
        print("Invalid choice. Please select between 1 and 5.")  # Handle wrong input
        input("\nPress Enter to continue...")
