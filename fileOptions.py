from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import *
import os

def openFile(root, textbox):
    filepath = askopenfilename(
        initialdir = "C:/Users/pgao2/",
        title = "Open Text File",
        filetypes = (("Text Files", "*.txt"),)
    )
    
    file = open(filepath)
    data = file.read()
    textbox.delete(1.0, END)
    textbox.insert(END, data)  
    file.close()

    fileName = os.path.basename(filepath)

    root.title(f"{os.path.splitext(fileName)[0]} - Notepad 2.0")
    
def saveAs(root, textbox):
    filepath = asksaveasfilename(
        defaultextension = "txt",
        filetypes = [("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not filepath:
        return

    with open(filepath, "w") as output_file:
        text = textbox.get(1.0, END)
        output_file.write(text)

    root.title(f"{filepath} - Notepad 2.0")