from tkinter import *

def fontMenu ():
    fontMenu = Toplevel()
    fontMenu.geometry("430x450")
    fontMenu.title("Font")
    fontMenu.resizable(False, False)
    fontMenu.grab_set()
    
    #font
    fontFrame = Frame(fontMenu)
    fontFrame.grid(column = 0, row = 0)

    font = Label(fontFrame, text = "Font:") 
    font.pack(side = TOP, anchor = W)

    fontEntry = Entry(fontFrame)
    fontEntry.pack(side = TOP, fill = BOTH)
    
    fontList = Listbox(fontFrame)
    fontList.pack(side = LEFT, fill = BOTH)

    fontList_yscroll = Scrollbar(fontFrame, orient = "vertical", command = fontList.yview)
    fontList_yscroll.pack(side = "right", fill = "both")
    fontList.configure(yscrollcommand = fontList_yscroll.set)

    #fontStyle
    fontStyleFrame = Frame(fontMenu)
    fontStyleFrame.grid(column = 1, row = 0)

    fontStyle = Label(fontStyleFrame, text = "Font Style:")
    fontStyle.pack(side = TOP, anchor = W)

    fontStyleEntry = Entry(fontStyleFrame)
    fontStyleEntry.pack(side = TOP, fill = BOTH)

    fontStyleList = Listbox(fontStyleFrame)
    fontStyleList.pack(side = LEFT, fill = BOTH)

    fontStyleList_yscroll = Scrollbar(fontStyleFrame, orient = "vertical", command = fontStyleList.yview)
    fontStyleList_yscroll.pack(side = RIGHT, fill = BOTH)
    fontStyleList.configure(yscrollcommand = fontStyleList_yscroll.set)

    #fontSize
    fontSizeFrame = Frame(fontMenu)
    fontSizeFrame.grid(column = 2, row = 0)

    fontSize = Label(fontSizeFrame, text = "Font Size:")
    fontSize.pack(side = TOP, anchor = W)
    fontSizeEntry = Entry(fontSizeFrame)
    fontSizeEntry.pack(side = TOP, fill = BOTH)
    fontSizeList = Listbox(fontSizeFrame)
    fontSizeList.pack(side = LEFT, fill = BOTH)

    fontSizeList_yscroll = Scrollbar(fontSizeFrame, orient = "vertical", command = fontSizeList.yview)
    fontSizeList_yscroll.pack(side = RIGHT, fill = BOTH)
    fontSizeList.configure(yscrollcommand = fontSizeList_yscroll.set)

    #sample
    sample = Label(fontMenu, text = "Sample")
    sample.grid(column = 1, row = 3)
    sampleFrame = Frame(fontMenu)
    sampleFrame.grid(column = 1, row = 4)
    sampleText = Label(sampleFrame, text = "AaBbYyZz")
    sampleText.pack()