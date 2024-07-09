# IF-ELSE

print("Type add, show, edit, done, help, exit.")

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
                                                                              
def addtask(command):
    # removing add to get the task
    if len(command) > 4:
        task = command[4:]
        tasks.append(task)
        update_file(tasks)
        print('Task added.')
    else:
        print("Please insert task after 'add' command")

def showtasks():
    print("\nShowing Tasks...")
    print("You have added", len(tasks), "tasks.")
    if len(tasks) != 0:
        print("Here are your tasks:")
    for i,task in enumerate(tasks):
        print(i+1, "-", task)

def edittask(command):
    if len(command) > 5:
        task_no = int(command[5:])
        if task_no > len(tasks) or task_no <1:
            print("ERROR: Task with this serial number doesn't exist.")
        else:
            old_task = tasks[task_no-1]
            print("Selected Task: ", old_task)
            new_task = input("Enter updated task: ")
            tasks[task_no-1] = new_task
            update_file(tasks)
            print("Task updated!")
    else:
        print("Please insert serial number after 'edit' command.")

def completetask(command):
    if len(command) > 5:
        task_no = int(command[5:])
        if task_no > len(tasks) or task_no <1:
            print("ERROR: Task with this serial number doesn't exist.")
        else:
            x_task = tasks.pop(task_no-1)
            update_file(tasks)
            print(f"'{x_task}' was removed from the tasks list.")
    else:
        print("Please insert serial number after 'done' command.")

while True:
    user_action = input("Enter a command: ")
    user_action = user_action.strip().lower()
    if "add" in user_action:
        addtask(user_action)
    elif "show" in user_action:
        showtasks()
    elif "edit" in user_action:
        edittask(user_action)
    elif "done" in user_action:
        completetask(user_action)
    elif "exit" in user_action:
        print("Exiting...")
        break
    elif "help" in user_action:
        print("\nType:\n'add' to add a task.\n'show' to get a list of entered tasks.\n'edit' to edit the task\n'done' or to remove a completed task\n'exit' to quit.")
    else:
        print("ERROR: Couldn't understand the command.")

print("Have a good day!")