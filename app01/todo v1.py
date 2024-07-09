# Match Case

status = True

print("Type add(a), show(s), edit(e), complete(c), help(h), exit.")

# writelines() doesn't add a new line -> so we added one
# readlines() adds a new line automatically
# everytime we are reading it we add a new line
# then we add another when we save it using the writelines() with added new line
# (print statement also displays a new line)
# therefore using read() which doesn't add newlines
# we could also use readlines() and strip the extra "\n"

def addtask_fromfile():
    print("Populating with tasks...")
    with open(r"app01/tasks.txt", "r") as f:
        tasks = f.read().splitlines()
    return tasks

tasks = addtask_fromfile()

def update_file(tasks_list):
    with open("app01/tasks.txt", "w") as f:
        f.writelines("%s\n" % t for t in tasks_list)
                                                                              
def addtask():
    task = input("\nEnter a task: ")
    tasks.append(task)
    update_file(tasks)
    print('Task added.')

def showtasks():
    print("\nShowing Tasks...")
    print("You have added", len(tasks), "tasks.")
    if len(tasks) != 0:
        print("Here are your tasks:")
    for t in tasks:
        print("-", t)

def edittask():
    print("\nWhich task to edit?")
    for i,task in enumerate(tasks):
        print(i+1, "-", task)
    task_no = int(input("Enter the serial number of the task: "))
    if task_no > len(tasks) or task_no <1:
        print("ERROR: Task with this serial number doesn't exist.")
    else:
        old_task = tasks[task_no-1]
        print("Selected Task: ", old_task)
        new_task = input("Enter updated task: ")
        tasks[task_no-1] = new_task
        update_file(tasks)
        print("Task updated!")

def completetask():
    print("\nWhich task did you complete?")
    for i,task in enumerate(tasks):
        print(i+1, "-", task)
    task_no = int(input("Enter the serial number of the task: "))
    if task_no > len(tasks) or task_no <1:
        print("ERROR: Task with this serial number doesn't exist.")
    else:
        x_task = tasks.pop(task_no-1)
        update_file(tasks)
        print(f"'{x_task}' was removed from the tasks list.")

while status:
    user_action = input("Enter a command: ")
    match user_action.strip().lower():
        case "add" | "a":
            addtask()
        case "show" | "s":
            showtasks()
        case "edit" | "e":
            edittask()
        case "complete" | "c":
            completetask()
        case "exit":
            print("Exiting...")
            status=False
        case "help" | "h":
            print("\nType:\n'add' or 'a' to add a task.\n'show' or 's' to get a list of entered tasks.\n'edit' or 'e' to edit the task\n'complete' or 'c' to remove a completed task\n'exit' to quit.")
        case _:
            print("ERROR: Couldn't understand the command.")

print("Have a good day!")