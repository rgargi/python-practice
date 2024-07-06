status = True
tasks = []

print("Type add(a), show, edit, help, exit.")

def addtask():
    task = input("Enter a task: ")
    tasks.append(task)
    print('Task added.')

def showtasks():
    print("Showing Tasks...")
    print("You have added", len(tasks), "tasks.")
    print("Here are your tasks:")
    for t in tasks:
        print("- ", t)

def edittask():
    print("Which task to edit?")
    for i,task in enumerate(tasks):
        print(i+1, "-", task)
    task_no = int(input("Enter the serial number of the task: "))
    if task_no > len(tasks) or task_no <1:
        print("ERROR: Task with this serial number doesn't exist.")
    else:
        old_task = tasks[task_no-1]
        print("Selected Task: ", old_task)
        new_task = input("Enter updated task: ")
        # tasks.remove(old_task)
        # tasks.insert(task_no-1, new_task)
        tasks[task_no-1] = new_task
        print("Task updated!")

while status:
    user_action = input("Enter a command: ")
    match user_action.strip().lower():
        case "add" | "a":
            addtask()
        case "show":
            showtasks()
        case "edit":
            edittask()
        case "exit":
            print("Exiting...")
            status=False
        case "help":
            print("Type:\n'add' to add a task.\n'show' to get a list of entered tasks.\n'edit' to edit the task\n'exit' to quit.")
        case _:
            print("ERROR: Couldn't understand the command.")

print("Have a good day!")