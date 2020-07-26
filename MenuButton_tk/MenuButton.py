from tkinter import *

root = Tk()

root.geometry('100x100')
menubutton = Menubutton(root, text = "Language", relief ="flat", background="#FE584C",)
menubutton.grid()
menubutton.menu = Menu(menubutton)
menubutton["menu"]=menubutton.menu
menubutton.menu.add_checkbutton(label = "Russian", variable=IntVar(), background="#ccc")
menubutton.menu.add_checkbutton(label = "English", variable=IntVar(), background="#ccc")
menubutton.pack()


root.mainloop()