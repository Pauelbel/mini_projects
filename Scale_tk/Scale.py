import tkinter as tk

def select():
    sel = "Value = " + str(v.get())
    label.config(text = sel)

root = tk.Tk()
root.geometry("200x100")
v = tk.DoubleVar()
scale = tk.Scale(root, variable = v, from_ = 1, to = 50,
orient = tk.HORIZONTAL)

scale.pack(anchor=tk.CENTER)

btn = tk.Button(root, text="Value", command=select)
btn.pack(anchor=tk.CENTER)

label = tk.Label(root)
label.pack()

root.mainloop()