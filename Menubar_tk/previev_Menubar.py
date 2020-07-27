from tkinter import *

root = Tk()
root.geometry("100x100")

def myfunc():
    Label(root, text="Save...").pack()

menubar = Menu(root)
m1 = Menu(menubar, tearoff=0)
m1.add_command(label="Save", command=myfunc)
m1.add_separator()
m1.add_command(label="Exit", command=quit)
menubar.add_cascade(label="File", menu=m1)
m2 = Menu(menubar, tearoff=0)
m2.add_command(label="Find", command=myfunc)
m2.add_separator()
m2.add_command(label="Exit", command=quit)
menubar.add_cascade(label="Edit", menu=m2)

root.config(menu=menubar)
root.mainloop()
