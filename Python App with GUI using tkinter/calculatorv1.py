from tkinter import *

root = Tk()

e1 = Entry(root, width = 10)
e1.grid(row = 0, column = 0)

e2 = Entry(root, width = 10)
e2.grid(row = 0, column = 1)

def add():
    num = int(e1.get()) + int(e2.get())
    l1 = Label(root, text = num)
    l1.grid(row = 2, column = 0)

def sub():
    num = int(e1.get()) - int(e2.get())
    l2 = Label(root, text = num)
    l2.grid(row = 2, column = 1)

def mul():
    num = int(e1.get()) * int(e2.get())
    l2 = Label(root, text = num)
    l2.grid(row = 2, column = 2)

def div():
    num = int(e1.get()) / int(e2.get())
    l2 = Label(root, text = num)
    l2.grid(row = 2, column = 3)

add = Button(root, text = " + ", width = 3, height = 2, command = add)
add.grid(row = 1, column = 0)

sub = Button(root, text = " - ", width = 3, height = 2, command = sub)
sub.grid(row = 1, column = 1)

mul = Button(root, text = " * ", width = 3, height = 2, command = mul)
mul.grid(row = 1, column = 2)

div = Button(root,text = " / ", width = 3, height = 2, command = div)
div.grid(row = 1, column = 4)

root.mainloop()
