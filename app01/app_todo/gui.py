from modules import functions as fn

from tkinter import *
from tkinter import ttk
import ctypes

# Increase Dots Per inch so it looks sharper
ctypes.windll.shcore.SetProcessDpiAwareness(True)

def add():
    new_task = task.get()
    if new_task != "":
        fn.addtask(new_task)
    task.set("")

# main window
window = Tk()
window.title("My To-Do App")
# make the window not resizable, since height and width is FALSE
window.resizable(height=FALSE, width=FALSE)

# the following code creates a frame
# grid places it directly inside main window 
# columnconfigure/rowconfigure bits tell Tk that the 
# frame should expand to fill any extra space if the window is resized

mainframe = ttk.Frame(window, padding="5 5 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

# create a widget, specify its parent and assign a variable to the widget
# The sticky option to grid describes how the widget should 
# line up within the grid cell, using compass directions. 
# So w (west) means to anchor the widget to the left side of the cell, 
# we (west-east) means to attach it to both the left and right sides, and so on.

ttk.Label(mainframe, text="Type in a task:", font=('Helvetica 12')).grid(column=1, row=1, sticky=(W, E))

task = StringVar()
task_entry = ttk.Entry(mainframe, width=40, textvariable=task, font=('Helvetica 14 bold')) # TODO: tooltip ??
task_entry.grid(column=1, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Add", command=add).grid(column=3, row=2)

# the following code walks through all of the widgets contained within our 
# content frame and adds a little bit of padding 
# puts the focus on our entry widget
# tells Tk that if a user presses the Enter key, it should call our calculate routine

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=2, pady=2)
task_entry.focus()
# window.bind("<Return>", calculate)

window.mainloop()