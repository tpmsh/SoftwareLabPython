from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text = "Look!, I clicked a Button")

myButton = Button(root,text = "Click Me!", padx = 50, pady = 75, command = myClick)
myButton.pack()

root.mainloop()
