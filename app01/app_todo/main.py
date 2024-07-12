# IF-ELIF-ELSE

from modules import functions as fn

# standard modules
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("\nIt is", now)
print("Type add, show, edit, done, help, exit")

while True:
    user_action = input("Enter a command: ")
    user_action = user_action.strip()
    if user_action.startswith("add"):
        fn.addtask(user_action)
    elif user_action.startswith("show"):
        fn.showtasks()
    elif user_action.startswith("edit"):
        fn.edittask(user_action)
    elif user_action.startswith("done"):
        fn.completetask(user_action)
    elif user_action.startswith("exit"):
        print("Exiting...")
        break
    elif user_action.startswith("help"):
        print("\nType:\n'add' to add a task.\n'show' to get a list of entered tasks.\n'edit' to edit the task\n'done' or to remove a completed task\n'exit' to quit.")
    else:
        print("ERROR: Couldn't understand the command.")

print("Have a good day!")