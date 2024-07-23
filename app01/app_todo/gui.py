from modules import functions as fn

from tkinter import *
from tkinter import ttk
import ctypes

# Increase Dots Per inch so it looks sharper
ctypes.windll.shcore.SetProcessDpiAwareness(True)

def refresh_listbox():
     get_list = fn.get_tasks()
     taskList.set(get_list)

def add_task():
    new_task = task.get()
    if new_task != "":
        msg = fn.addtask(new_task)
        task.set("")
        refresh_listbox()
        displayMessage.set(msg)

def show_task(_):
    selected_task = lb_tasklist.selection_get()
    task.set(selected_task)

def edit_task():
    try:
        selected_task = lb_tasklist.selection_get()
        editted_task = task.get()
        if selected_task != editted_task:
            index = lb_tasklist.curselection()[0]
            msg = fn.edittask(index, editted_task)
            refresh_listbox()
        else:
             msg = "You can make changes to the content of the task"
    except TclError as err:
         print(err)
         msg = "You need to select a task from the list"
    displayMessage.set(msg)

def complete_task(_):
        index = lb_tasklist.curselection()[0]
        msg = fn.completetask(index)    
        refresh_listbox()
        displayMessage.set(msg)

# main window
window = Tk()
window.title("My To-Do App")
# make the window not resizable, since height and width is FALSE
window.resizable(height=FALSE, width=FALSE)

# declare variables
displayMessage = StringVar()
task = StringVar()
taskList = StringVar(value=fn.get_tasks())

# the following code creates a frame
# grid places it directly inside main window 
# columnconfigure/rowconfigure bits tell Tk that the 
# frame should expand to fill any extra space if the window is resized

# outer frame
mainframe = ttk.Frame(window, padding="5 5 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

# create a widget, specify its parent and assign a variable to the widget
# The sticky option to grid describes how the widget should 
# line up within the grid cell, using compass directions. 
# So w (west) means to anchor the widget to the left side of the cell, 
# we (west-east) means to attach it to both the left and right sides, and so on.

# create widgets
lbl_header = ttk.Label(mainframe, text="Type in a task:", font=('Helvetica 12'))
entry_task = ttk.Entry(mainframe, width=40, textvariable=task, exportselection=False, font=('Helvetica 14 bold')) 
bt_add = ttk.Button(mainframe, text="Add", command=add_task)
lb_tasklist = Listbox(mainframe, listvariable=taskList, width=40)
bt_edit = ttk.Button(mainframe, text="Edit", command=edit_task)
lbl_msg = ttk.Label(mainframe, textvariable=displayMessage, font=("Corbel 10"))

# grid all the widgets
lbl_header.grid(column=1, row=1, sticky=(W, E))
entry_task.grid(column=1, row=2, sticky=(W, E))
bt_add.grid(column=3, row=2)
lb_tasklist.grid(column=1, sticky=(W,E))
bt_edit.grid(column=3, row=3)
lbl_msg.grid(column=1, row=4, sticky=(W,E))

# the following code walks through all of the widgets contained within our 
# content frame and adds a little bit of padding 
# puts the focus on our entry widget
# tells Tk that if a user presses the Enter key, it should call our calculate routine

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=2, pady=2)

# Set event bindings 
# for when the selection in the listbox changes,
# when the user double clicks the list, and when they hit the Return key

entry_task.focus()
lb_tasklist.bind('<<ListboxSelect>>', show_task)
lb_tasklist.bind('<Double-1>', complete_task)

window.mainloop()