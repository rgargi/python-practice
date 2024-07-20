from modules import functions as fn

from tkinter import *
from tkinter import ttk

# main window
root = Tk()
root.title("My To-Do App")

# frame created
# grid places it directly inside main window 
# columnconfigure/rowconfigure bits tell Tk that the 
# frame should expand to fill any extra space if the window is resized

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# create a widget, specify its parent and assign a variable to the widget
# The sticky option to grid describes how the widget should 
# line up within the grid cell, using compass directions. 
# So w (west) means to anchor the widget to the left side of the cell, 
# we (west-east) means to attach it to both the left and right sides, and so on.

ttk.Label(mainframe, text="Type in a task:").grid(column=1, row=1, sticky=(W, E))

task = StringVar()
task_entry = ttk.Entry(mainframe, width=40, textvariable=task) # TODO: tooltip ??
task_entry.grid(column=1, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Add", command=print(task)).grid(column=3, row=2)

root.mainloop()