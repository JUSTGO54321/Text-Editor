from tkinter import *

def replaceMenu ():
    replaceMenu = Toplevel()
    replaceMenu.geometry("370x150")
    replaceMenu.title("Replace")
    replaceMenu.resizable(False, False)
    replaceMenu.grab_set

    find = Label(replaceMenu, text = "Find:")
    find.grid(column = 0, row = 0)
    findEntry = Entry(replaceMenu)
    findEntry.grid(column = 1, row = 0)

    replaceWith = Label(replaceMenu, text = 'Replace With:')
    replaceWith.grid(column = 0, row = 1)
    replaceWithEntry = Entry(replaceMenu)
    replaceWithEntry.grid(column = 1, row = 1)

    matchCase = Checkbutton(replaceMenu, text = "Match case")
    matchCase.grid(column = 0, row = 2)

    wrapAround = Checkbutton(replaceMenu, text = "Wrap around")
    wrapAround.grid(column = 0, row = 3) #fix margin issue to make this appear!

    buttonFrame = Frame(replaceMenu)
    buttonFrame.grid(column = 3, row = 0)

    findNext = Button(buttonFrame, text = "Find Next")
    findNext.pack()

    replace = Button(buttonFrame, text = "Replace")
    replace.pack()

    replaceAll = Button(buttonFrame, text = "Replace All")
    replaceAll.pack()

    cancel = Button(buttonFrame, text = "Cancel", command = replaceMenu.destroy)
    cancel.pack()