FILEPATH = r"tasks.txt"

# writelines() doesn't add a new line -> so we added one
# readlines() adds a new line automatically
# everytime we are reading it we add a new line
# then we add another when we save it using the writelines() with added new line
# (print statement also displays a new line)
# therefore using read() which doesn't add newlines
# we could also use readlines() and strip the extra "\n"

def get_tasks(filepath=FILEPATH):
    """Get tasks from the the file."""
    with open(filepath, "r") as f:
        tasks_data = f.read().splitlines()
    return tasks_data

def update_file(tasks_list, filepath=FILEPATH):
    """ Update the file with changes. Run after adding a new task, 
    editing a task, and deleting a completed task."""
    update_done = 0
    try:
        with open(filepath, "w") as f:
            f.writelines("%s\n" % t for t in tasks_list)
        update_done = 1
    except UnicodeEncodeError as err:
        update_done = 0
        print("You entered characters which cannot be encoded.")
    return update_done
                                                                              
def addtask(command):
    tasks = get_tasks()
    # removing 'add' to get the task
    if len(command) > 4:
        task = command[4:]
        tasks.append(task)
        if update_file(tasks) == 1:
            print('Task added.')
        else:
            print("Task couldn't be added.")
    else:
        print("Please insert task after 'add' command")

def showtasks():
    print("\nShowing Tasks...")
    tasks = get_tasks()
    print("You have added", len(tasks), "tasks.")
    if len(tasks) != 0:
        print("Here are your tasks:")
    for i,task in enumerate(tasks):
        print(i+1, "-", task)

def edittask(command):
    tasks = get_tasks()
    try: 
        if len(command) > 5:
            task_no = int(command[5:])
            if task_no > len(tasks) or task_no <1:
                print("ERROR: Task with this serial number doesn't exist.")
            else:
                old_task = tasks[task_no-1]
                print("Selected Task: ", old_task)
                new_task = input("Enter updated task: ")
                tasks[task_no-1] = new_task
                if update_file(tasks) == 1:
                    print("Task updated!")
                else:
                    print("Task couldn't be updated.")
        else:
            print("Please insert serial number after 'edit' command.")
    except ValueError as err:
        print("Only insert a number after 'edit' command.")

def completetask(command):
    tasks = get_tasks()
    try:
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
    except ValueError as err:
         print("Only insert a number after 'done' command.")

print("Loading functions...")
if __name__ == "__main__":
    print("Only run when running this file directly")
    print("Will not run when running this file indirectly from main.py")
    print(__name__)