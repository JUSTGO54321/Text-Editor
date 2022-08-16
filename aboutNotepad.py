from tkinter import *

def about():
    about = Toplevel()

    about.title("About Notepad 2.0")
    about.geometry("700x350")
    about.resizable(False, False)
    about.grab_set()

    btn = Button(about, text = "OK", command = about.destroy)
    btn.pack(anchor = SE)