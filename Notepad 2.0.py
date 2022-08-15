from tkinter import *
from tkinter.filedialog import *
from fontMenu import fontMenu
from replaceMenu import replaceMenu

def saveAs():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes = [("Text Files", "*.txt"),
        ("All Files", "*.*")]
    )

    if not filepath:
        return

    with open(filepath, "w") as output_file:
        text = textbox.get(1.0, END)
        output_file.write(text)

    root.title(f"Entitled - {filepath}")

def openFile():
    tf = askopenfilename(
        initialdir = "C:/Users/pgao2/",
        title = "Open Text File",
        filetypes = (("Text Files", "*.txt"),)
    )

    tf = open(tf)
    data = tf.read()
    textbox.insert(END, data)
    tf.close()

root = Tk()

root.title("Untitled - Notepad 2.0")
root.geometry("700x350")

#xscroll creation
textbox_xscroll = Scrollbar(root, orient = HORIZONTAL)
textbox_xscroll.pack(side = BOTTOM, fill = X)

#yscroll creation
textbox_yscroll = Scrollbar(root)
textbox_yscroll.pack(side = RIGHT, fill = Y)

#textbox creation
textbox = Text(root, font = ("Calibri, 11"))
textbox.configure(xscrollcommand = textbox_xscroll.set, yscrollcommand = textbox_yscroll.set)
textbox.pack(fill = BOTH, expand = 1, side = LEFT)

#scrollbars' function
textbox_xscroll.config(command = textbox.xview)
textbox_yscroll.config(command = textbox.yview)

#menu
menu = Menu(root)
root.config(menu = menu)

filemenu = Menu(menu, tearoff = 0)
menu.add_cascade(label = 'File', menu = filemenu)
filemenu.add_command(label = 'New', accelerator = "Ctrl+N")
filemenu.add_command(label = 'New Window', accelerator = 'Ctrl+Shift+N')
filemenu.add_command(label = 'Open...', accelerator = 'Ctrl+O', command = openFile)
root.bind('<Control-o>', lambda event: openFile())
filemenu.add_command(label = 'Save', accelerator = 'Ctrl+S')
filemenu.add_command(label = 'Save As', accelerator = 'Ctrl+Shift+S', command = saveAs)
root.bind("<Control-Shift-S>", lambda event: saveAs())
filemenu.add_separator()
filemenu.add_command(label = 'Page Setup...')
filemenu.add_command(label = 'Print', accelerator = 'Ctrl+P')
filemenu.add_separator()
filemenu.add_command(label = 'Exit', command=root.quit)

editmenu = Menu(menu, tearoff = 0)
menu.add_cascade(label = 'Edit', menu = editmenu)
editmenu.add_command(label = 'Undo', accelerator = 'Ctrl+Z')
editmenu.add_separator()
editmenu.add_command(label = 'Cut', accelerator = 'Ctrl+X')
editmenu.add_command(label = 'Copy', accelerator = 'Ctrl+C')
editmenu.add_command(label = 'Paste', accelerator = 'Ctrl+V')
editmenu.add_command(label = 'Delete', accelerator = 'Del')
editmenu.add_separator()
editmenu.add_command(label = 'Search with Opera GX (work in progress)', accelerator = 'Ctrl+E')
editmenu.add_command(label = 'Find...', accelerator = 'Ctrl+F')
editmenu.add_command(label = 'Find Next', accelerator = 'F3')
editmenu.add_command(label = 'Find Previous', accelerator = 'Shift+F3')
editmenu.add_command(label = 'Replace...', accelerator = 'Ctrl+H', command = replaceMenu)
editmenu.add_command(label = 'Go To...', accelerator = 'Ctrl+G')
editmenu.add_separator()
editmenu.add_command(label = 'Select All', accelerator = 'Ctrl+A')
editmenu.add_command(label = 'Time/Date', accelerator = 'F5')


formatmenu = Menu(menu, tearoff = 0)
menu.add_cascade(label = 'Format', menu = formatmenu)
formatmenu.add_radiobutton(label = 'Word Wrap')
formatmenu.add_command(label = 'Font...', command = fontMenu)

viewmenu = Menu(menu, tearoff = 0)
menu.add_cascade(label = 'View', menu = viewmenu)
zoommenu = Menu(viewmenu, tearoff = 0)
viewmenu.add_cascade(label = 'Zoom', menu = zoommenu)
zoommenu.add_command(label = 'Zoom In', accelerator = 'Ctrl+Plus')
zoommenu.add_command(label = 'Zoom out', accelerator = 'Ctrl+Minus')
zoommenu.add_command(label = 'Restore Default Zoom', accelerator = 'Ctrl+0')
viewmenu.add_checkbutton(label = 'Check Status')


helpmenu = Menu(menu, tearoff = 0)
menu.add_cascade(label = 'Help', menu = helpmenu)
helpmenu.add_command(label = 'View Help')
helpmenu.add_command(label = 'Send Feedback')
helpmenu.add_separator()
helpmenu.add_command(label = 'About Notepad')

root.mainloop()