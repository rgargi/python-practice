import time

from tkinter import *
from tkinter import ttk
from tkinter import filedialog

import ctypes

# Increase Dots Per inch so it looks sharper
ctypes.windll.shcore.SetProcessDpiAwareness(True)

# colors for the application
primary = '#081F4D'
secondary = '#0083FF'
white = '#FFFFFF'

def init():
    now = time.strftime("%b %d, %Y %H:%M")
    displayMessage.set(f"It is {now}")
    # print("\nIt is", now)

def choose_files():
    selectedFiles = filedialog.askopenfilenames()
    filenames.set(selectedFiles)

def choose_folder():
    selectedFolder = filedialog.askdirectory()
    foldername.set(selectedFolder)

def archive_files():
    # displayMessage.set("Compressed Files!")
    displayMessage.set("Archive Created!")
    print("Files Compressed")

# main window
window = Tk()
window.title("Compress Files")

# variables
displayMessage = StringVar()
filenames = StringVar()
foldername = StringVar()

init()

# frame
mainframe = ttk.Frame(window, padding="4 4 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

window.columnconfigure(2, weight=1)
window.rowconfigure(3, weight=1)

# widgets
ttk.Label(mainframe, text="Select Files to Compress:").grid(column=1, row=1, sticky=(W))
ttk.Entry(mainframe, width=50, textvariable=filenames).grid(column=2, row=1)
ttk.Button(mainframe, text="Choose", command=choose_files).grid(column=3, row=1)

ttk.Label(mainframe, text="Select Destination Folder:").grid(column=1, row=2, sticky=(W))
ttk.Entry(mainframe, width=50, textvariable=foldername).grid(column=2, row=2)
ttk.Button(mainframe, text="Choose", command=choose_folder).grid(column=3, row=2)

ttk.Button(mainframe, text="COMPRESS", command=archive_files).grid(column=1, row=3, sticky=(W))
ttk.Label(mainframe, textvariable=displayMessage, font=('Bold'), foreground=secondary).grid(column=2, row=3)

window.mainloop()