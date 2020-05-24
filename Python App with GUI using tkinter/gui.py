from tkinter import *

root = Tk()

myLabel1 = Label(root, text = "Hello, World!")
myLabel2 = Label(root, text = "My Name is Prathamesh")
myLabel3 = Label(root, text = "How are you?")
# Shove it
myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 2, column = 2)
myLabel3.grid(row = 1, column = 1)
#Event Loop is continually Loop
#program ends, loop ends
root.mainloop()
