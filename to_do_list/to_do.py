# | **Beginner** | **Console/CLI** | **8. To-Do List (CLI)** | Lists, basic file I/O (`.txt` file) for storage. |
# This is a file based CLI controlled to-do list program, so that yu don't lose your task list

file = 'file.txt'

# Loading the existing tasks in the file
def load_tasks():
    try:
        with open(file, 'r') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []
    
# Function to print tasks 
def read_tasks(tasks):
    if not tasks:
        print("\n------List is Empty------")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    print('-'*25)

# Function to save tasks
def save_all_tasks(tasks):
    with open(file, 'w') as f:
        for task in tasks:
            f.write(task + '\n')


list_of_tasks = load_tasks()

while True:
    query = input("What operation you want to perform? (create/read/delete/exit) task : ").lower()

    if query == 'create':
        entry_task = input("Enter the task you want to enter : ")
        list_of_tasks.append(entry_task)
        with open(file, 'a') as f:
            f.write(entry_task + '\n')
        print('Task added!')

    elif query == 'read':
        read_tasks(list_of_tasks)

    elif query == 'delete':
        try:
            index = int(input("Enter the # of task you want to remove? : "))
            removed = list_of_tasks.pop(index-1)
            save_all_tasks(list_of_tasks)
            print(f"Deleted : {removed}")
        except (ValueError, IndexError):
            print("Invalid number! Please look at the list again.")

    elif query == 'exit':
        print("Closing To-Do List. Goodbye!")
        break
    else:
        print("Invalid entry. Please type 'create', 'read', 'delete', or 'exit'.")

