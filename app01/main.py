status = True
tasks = []

print("Type:\n'add' to add a task.\n'show' to get a list of entered tasks.\n'help' for supported commands.\n'exit' to quit.")

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

while status:
    user_action = input("Enter a command: ")
    match user_action.lower():
        case "add":
            addtask()
        case "show":
            showtasks()
        case "exit":
            print("Exiting...")
            status=False
        case "help":
            print("Type:\n'add' to add a task.\n'show' to get a list of entered tasks.\n'exit' to quit.")
        case _:
            print("Couldn't understand.")
