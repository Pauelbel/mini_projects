from tkinter import *
root = Tk()
root.geometry('290x200')
uname = Label(root, text="Username").place(x=30, y=50)
password = Label(root, text="Password").place(x=30, y=90)
bttn = Button(root, text="Submit", activebackground="pink",
              activeforeground="blue").place(x=30, y=120)

e1 = Entry(root, width=30).place(x=100, y=50)
e2 = Entry(root, width=30).place(x=100, y=90)

root.mainloop()
