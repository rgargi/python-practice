# Some example scripts using the third party module FreeSimpleUI

import FreeSimpleGUI as sg

feet_label = sg.Text("Enter feet: ")
feet_input = sg.Input()

inches_label = sg.Text("Enter inches: ")
inches_input = sg.Input()

button = sg.Button("Convert")

window = sg.Window("Convertor",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [button]])

window.read()
window.close()

# --------------------------------------------------

# pysimplegui example

import PySimpleGUI as sg
from converters import convert

sg.theme("Black")

feet_label = sg.Text("Enter feet: ")
feet_input = sg.Input(key="feet")

inches_label = sg.Text("Enter inches: ")
inches_input = sg.Input(key="inches")

button = sg.Button("Convert")
output_label = sg.Text("", key="output")
exit_button = sg.Button("Exit")

window = sg.Window("Convertor",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [button, exit_button, output_label]])

while True:
    event, values = window.read()
    match event:
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = convert(feet, inches)
    window["output"].update(value=f"{result} m", text_color="white")


window.close()

# --------------------------------------------------

# example where the widgets are aligned

import PySimpleGUI as sg

# from zip_extractor import extract_archive
 
sg.theme("Black")
 
label1 = sg.Text("Select archive:")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="archive")
 
label2 = sg.Text("Select destination directory:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")
 
extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")
 
col1 = sg.Column([[label1], [label2]])
col2 = sg.Column([[input1], [input2]])
col3 = sg.Column([[choose_button1], [choose_button2]])
 
window = sg.Window("Archive Extractor",
                   layout=[[col1, col2, col3], [extract_button]])
while True:
    event, values = window.read()
    print(event, values)
    archivepath = values["archive"]
    dest_dir = values["folder"]
    extract_archive(archivepath, dest_dir)
    window["output"].update(value="Extraction Completed!")
 
window.close()