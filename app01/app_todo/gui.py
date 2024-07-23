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

def show_task(*args):
    selected_task = wd_tasklistbox.selection_get()
    task.set(selected_task)

def edit_task():
    try:
        selected_task = wd_tasklistbox.selection_get()
        editted_task = task.get()
        if selected_task != editted_task:
            index = wd_tasklistbox.curselection()[0]
            msg = fn.edittask(index, editted_task)
            refresh_listbox()
        else:
             msg = "You can make changes to the content of the task"
    except TclError as err:
         print(err)
         msg = "You need to select a task from the list"
    displayMessage.set(msg)

def add_or_edit_task(*args):
    selection = wd_tasklistbox.curselection()
    # task_box_entry = task.get()
    if len(selection) == 0:
        add_task()
    elif len(selection) == 1:
        edit_task()
    else:
         msg = "Woah! What did you press?!"
         displayMessage.set(msg)

def complete_task(*args):
        index = wd_tasklistbox.curselection()[0]
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

# ui variables
main_color = "#007f5c"
sec_color = "#3cb371"

# style
style = ttk.Style(window)
style.theme_use("alt")

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
wd_header = ttk.Label(mainframe, text="Type in a task:", font=('Arial 10'))
wd_entry_task = ttk.Entry(mainframe, width=35, textvariable=task, exportselection=False, font=('Corbel 14 bold')) 
bt_add = ttk.Button(mainframe, text="Add", command=add_task)
wd_tasklistbox = Listbox(mainframe, listvariable=taskList, width=35, font=('Corbel 12'), selectbackground=main_color)
wd_taskscroll = ttk.Scrollbar(mainframe, orient=VERTICAL, command=wd_tasklistbox.yview)
bt_edit = ttk.Button(mainframe, text="Edit", command=edit_task)
bt_done = ttk.Button(mainframe, text="Clear Task", command=complete_task)
bt_exit = ttk.Button(mainframe, text="Exit", command=exit)
wd_msg = ttk.Label(mainframe, textvariable=displayMessage, font=("Arial 10"), foreground=sec_color)

# grid all the widgets
wd_header.grid(column=1, row=1, sticky=(W, E))
wd_entry_task.grid(column=1, row=2, sticky=(W, E))
bt_add.grid(column=3, row=2)
wd_tasklistbox.grid(column=1, sticky=(W,E))
wd_taskscroll.grid(column=2, row=3, sticky=(N,S))
bt_edit.grid(column=3, row=3, sticky=(N))
bt_done.grid(column=3, row=3, sticky=(S))
bt_exit.grid(column=3, row=4)
wd_msg.grid(column=1, row=4, sticky=(W,E))

# further configuration
wd_tasklistbox.configure(yscrollcommand=wd_taskscroll.set)

# the following code walks through all of the widgets contained within our 
# content frame and adds a little bit of padding 
# puts the focus on our entry widget
# tells Tk that if a user presses the Enter key, it should call our calculate routine

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=3, pady=3)

# Set event bindings 
# for when the selection in the listbox changes,
# when the user double clicks the list, and when they hit the Return key

def change_focus(*args):
    wd_entry_task.focus()

wd_entry_task.focus()
wd_tasklistbox.bind('<<ListboxSelect>>', show_task)
wd_tasklistbox.bind('<Double-1>', complete_task)
wd_tasklistbox.bind('<Return>', change_focus)
wd_entry_task.bind('<Return>', add_or_edit_task)

window.mainloop()