from std_modules import std_zipfile as z

from tkinter import *
from tkinter import ttk
from tkinter import filedialog

import ctypes

# Increase Dots Per inch so it looks sharper
ctypes.windll.shcore.SetProcessDpiAwareness(True)

# colors for the application
primary = '#081F4D'
secondary = '#0083FF'

def init():
    displayMessage.set("Hello!")

def choose_files():
    selectedFiles = filedialog.askopenfilenames()
    displayMessage.set("Selected files to unarchive")
    filenames.set(selectedFiles)

def choose_folder():
    selectedFolder = filedialog.askdirectory()
    displayMessage.set("Selected destination folder")
    foldername.set(selectedFolder)

def extract_files():
    paths = []
    unedited_paths = filenames.get().strip("()").split(",")
    for p in unedited_paths:
        p = p.strip("'").strip(" ").strip("'")
        paths.append(p)
    dd = foldername.get()
    z.extract_archive(filepaths=paths, destination_dir=dd)
    displayMessage.set("Extracted Files!")
    
# main window
window = Tk()
window.title("Extract Files")

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
ttk.Label(mainframe, text="Select Files to Extract:").grid(column=1, row=1, sticky=(W))
ttk.Entry(mainframe, width=50, textvariable=filenames).grid(column=2, row=1)
ttk.Button(mainframe, text="Choose", command=choose_files).grid(column=3, row=1)

ttk.Label(mainframe, text="Select Destination Folder:").grid(column=1, row=2, sticky=(W))
ttk.Entry(mainframe, width=50, textvariable=foldername).grid(column=2, row=2)
ttk.Button(mainframe, text="Choose", command=choose_folder).grid(column=3, row=2)

ttk.Button(mainframe, text="Extract", command=extract_files).grid(column=1, row=3, sticky=(W))
ttk.Label(mainframe, textvariable=displayMessage, font=('Bold'), foreground=secondary).grid(column=2, row=3)

window.mainloop()