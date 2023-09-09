from tkinter import *
from tkinter.filedialog import *
from fontMenu import fontMenu
from replaceMenu import replaceMenu
from aboutNotepad import about
from fileOptions import *
import webbrowser

class App(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        master.title("Untitled - Notepad 2.0")
        master.geometry("700x350")

        #xscroll creation
        self.textbox_xscroll = Scrollbar(self, orient = HORIZONTAL)
        self.textbox_xscroll.pack(side = BOTTOM, fill = X)

        #yscroll creation
        self.textbox_yscroll = Scrollbar(self)
        self.textbox_yscroll.pack(side = RIGHT, fill = Y)

        #textbox creation
        self.textbox = Text(self, font = ("Calibri, 11"))
        self.textbox.configure(xscrollcommand = self.textbox_xscroll.set, yscrollcommand = self.textbox_yscroll.set)
        self.textbox.pack(fill = BOTH, expand = 1, side = LEFT)

        #scrollbars' function
        self.textbox_xscroll.config(command = self.textbox.xview)
        self.textbox_yscroll.config(command = self.textbox.yview)

        #menu
        self.menu = Menu(self)
        self.master.config(menu = self.menu)

        self.filemenu = Menu(self.menu, tearoff = 0)
        self.menu.add_cascade(label = 'File', menu = self.filemenu)
        self.filemenu.add_command(label = 'New', accelerator = "Ctrl+N")
        self.filemenu.add_command(label = 'New Window', accelerator = 'Ctrl+Shift+N')
        self.filemenu.add_command(label = 'Open...', accelerator = 'Ctrl+O', command = lambda: openFile(master, self.textbox))
        master.bind('<Control-o>', lambda event: openFile(master, self.textbox))
        self.filemenu.add_command(label = 'Save', accelerator = 'Ctrl+S')
        self.filemenu.add_command(label = 'Save As', accelerator = 'Ctrl+Shift+S', command = lambda: saveAs(master, self.textbox))
        master.bind("<Control-Shift-S>", lambda event: saveAs(master, self.textbox))
        self.filemenu.add_separator()
        self.filemenu.add_command(label = 'Page Setup...')
        self.filemenu.add_command(label = 'Print', accelerator = 'Ctrl+P')
        self.filemenu.add_separator()
        self.filemenu.add_command(label = 'Exit', command = master.quit)

        self.editmenu = Menu(self.menu, tearoff = 0)
        self.menu.add_cascade(label = 'Edit', menu = self.editmenu)
        self.editmenu.add_command(label = 'Undo', accelerator = 'Ctrl+Z')
        self.editmenu.add_separator()
        self.editmenu.add_command(label = 'Cut', accelerator = 'Ctrl+X')
        self.editmenu.add_command(label = 'Copy', accelerator = 'Ctrl+C')
        self.editmenu.add_command(label = 'Paste', accelerator = 'Ctrl+V')
        self.editmenu.add_command(label = 'Delete', accelerator = 'Del')
        self.editmenu.add_separator()
        self.editmenu.add_command(label = 'Search with Opera GX (work in progress)', accelerator = 'Ctrl+E')
        self.editmenu.add_command(label = 'Find...', accelerator = 'Ctrl+F')
        self.editmenu.add_command(label = 'Find Next', accelerator = 'F3')
        self.editmenu.add_command(label = 'Find Previous', accelerator = 'Shift+F3')
        self.editmenu.add_command(label = 'Replace...', accelerator = 'Ctrl+H', command = replaceMenu)
        master.bind("<Control-h>", lambda event: replaceMenu())
        self.editmenu.add_command(label = 'Go To...', accelerator = 'Ctrl+G')
        self.editmenu.add_separator()
        self.editmenu.add_command(label = 'Select All', accelerator = 'Ctrl+A')
        self.editmenu.add_command(label = 'Time/Date', accelerator = 'F5')

        self.formatmenu = Menu(self.menu, tearoff = 0)
        self.menu.add_cascade(label = 'Format', menu = self.formatmenu)
        self.formatmenu.add_radiobutton(label = 'Word Wrap')
        self.formatmenu.add_command(label = 'Font...', command = fontMenu)

        self.viewmenu = Menu(self.menu, tearoff = 0)
        self.menu.add_cascade(label = 'View', menu = self.viewmenu)
        self.zoommenu = Menu(self.viewmenu, tearoff = 0)
        self.viewmenu.add_cascade(label = 'Zoom', menu = self.zoommenu)
        self.zoommenu.add_command(label = 'Zoom In', accelerator = 'Ctrl+Plus')
        self.zoommenu.add_command(label = 'Zoom out', accelerator = 'Ctrl+Minus')
        self.zoommenu.add_command(label = 'Restore Default Zoom', accelerator = 'Ctrl+0')
        self.viewmenu.add_checkbutton(label = 'Check Status')

        self.helpmenu = Menu(self.menu, tearoff = 0)
        self.menu.add_cascade(label = 'Help', menu = self.helpmenu)
        self.helpmenu.add_command(label = 'View Help', command = lambda: webbrowser.open("https://www.google.com/search?q=get help with notepad in windows"))
        self.helpmenu.add_command(label = 'Send Feedback')
        self.helpmenu.add_separator()
        self.helpmenu.add_command(label = 'About Notepad', command = about)

    def newWindow(self):
        self.newWindow = Toplevel(self.master)        
        self.fontMenu = FontMenu(self.newWindow)
        self.replaceMenu = ReplaceMenu(self.newWindow)

class FontMenu(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master

class ReplaceMenu(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master

if __name__ == "__main__":
    root = Tk()
    App(root).pack(side="top", fill="both", expand=True)
    root.mainloop()