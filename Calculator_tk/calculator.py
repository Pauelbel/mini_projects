""" Подгружаем библиотеку, бокс выводящий сообщения об ошибках,
обновленные кнопки и модуль для работы с числами """

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import math

""" Cоздаем окно верхнего уровня, указываем его название и
конфигурацию """

root = tk.Tk()  # окно
root.title("Калькулятор")  # название окна
root.configure(background="deepskyblue", bd=3)

"""Мозг калькулятора"""

def calk(key):
#  Обозначаем символы доступные для использования
    if key == "=":
        strl = "+-0123456789*/xⁿ+/-cos()math radian grad sin tan n!п M"
#  Если введены символы не включенные в strl получим ошибку
        if calc_entry.get()[0] not in strl:
            calc_entry.insert(tk.END, " -> Введите число!")
            messagebox.showerror(" ошибка", "вы не ввели число")
#  Создаем исключение
        try:
            result = eval(calc_entry.get())
            calc_entry.delete(0, tk.END)
            calc_entry.insert(tk.END, str(result))
        except:
            calc_entry.insert(tk.END, " -> ошибка")
            messagebox.showerror("ошибка", "проверь еще разок")
#  Очистить
    elif key == "C":
        calc_entry.delete(0, tk.END)
#  Замена + на -
    elif key == "+/-":
        if "=" in calc_entry.get():
            calc_entry.delete(0, tk.END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass
#  Синус угла, задаваемого в радианах
    elif key == "sin":
        calc_entry2.insert(0, 0)
        calc_entry2.delete(0, tk.END)
        calc_entry2.insert(0, str(format(math.sin(math.radians(float(
            calc_entry.get()))), ".15f")))
#  Косинус угла, задаваемого в радианах
    elif key == "cos":
        calc_entry2.insert(0, 0)
        calc_entry2.delete(0, tk.END)
        calc_entry2.insert(0, str(format(math.cos(math.radians(float(
            calc_entry.get()))), ".15f")))
#  Тангенс угла, задаваемого в радианах
    elif key == "tan":
        calc_entry2.insert(0, 0)
        calc_entry2.delete(0, tk.END)
        calc_entry2.insert(0, str(format(math.tan(math.radians(float(
            calc_entry.get()))), ".15f")))
#  Факториал
    elif key == "n!":
        calc_entry2.insert(0, 0)
        calc_entry2.delete(0, tk.END)
        calc_entry2.insert(0, str(math.factorial(int(calc_entry.get()))))
#  Константа π 
    elif key == "п":
        calc_entry.insert(tk.END, math.pi)
#  Возведение числа в степень
    elif key == "xⁿ":
        calc_entry.insert(tk.END, "**")
#  Выход из калькулятора
    elif key == "Exit":
        root.after(1, root.destroy)
        exit
#  Преобразует угол, заданный в градусах, в радианы.
    elif key == "rad":
        calc_entry2.insert(0, 0)
        calc_entry2.delete(0, tk.END)
        calc_entry2.insert(tk.END, str(
            math.radians(float((calc_entry.get())))))
#  Преобразует угол, заданный в радианах, в градусы.
    elif key == "grad":
        calc_entry2.insert(0, 0)
        calc_entry2.delete(0, tk.END)
        calc_entry2.insert(tk.END, str(
            math.degrees(float((calc_entry.get())))))
#  Квадратный корень
    elif key == "√2":
        calc_entry2.insert(0, 0)
        calc_entry2.delete(0, tk.END)
        calc_entry2.insert(tk.END, str(math.sqrt(float(calc_entry.get()))))
#  Добавление текущего значения в память
    elif key == "M+":
        calc_entry1.insert(0, 0)
        a = str(float(calc_entry.get()) + float(calc_entry1.get()))
        calc_entry1.delete(0, tk.END)
        calc_entry1.insert(tk.END, a)
#  Удаление текущего значения в память
    elif key == "M-":
        calc_entry1.insert(0, 0)
        calc_entry1.delete(0, tk.END)
        calc_entry1.insert(tk.END, calc_entry.get())
#  Добавление данных из пямяти в решение
    elif key == "R1":
        calc_entry.insert(tk.END, calc_entry1.get())
#  Добавление данных из пямяти в решение
    elif key == "R2":
        calc_entry.insert(tk.END, calc_entry2.get())
#  Очистить всю память
    elif key == "Cm":
        calc_entry1.delete(0, tk.END)
        calc_entry2.delete(0, tk.END)
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, tk.END)
        calc_entry.insert(tk.END, key)


"Создаем кнопки калькулятора"

bttn = [
    "7", "8", "9", "+", "-",
    "4", "5", "6", "*", "/",
    "1", "2", "3", "+/-", ".",
    "0", "xⁿ", "(", ")", "п",
    "grad", "sin", "cos", "tan", "n!",
    "rad", "√2", "M-", "M+", "R1",
    "C", "Cm", "Exit", "=", "R2"
]
r = 3
c = 0

"Цикл, перебирающий список кнопок bttn"

for i in bttn:
    def cmd(x=i): return calk(x)
    ttk.Button(root, text=i, command=cmd, width=8).grid(row=r, column=c)
    tk.Button(root, text=i, command=cmd, width=7,
              bg="deep sky blue").grid(row=r, column=c)
    c += 1
    if c > 4:
        c = 0
        r += 1
    elif i == "Exit":
        tk.Button(root, text="Exit", command=cmd, width=7,
                  pady="1", bg="gray").grid(row=9, column=2)
    elif i == "=":
        tk.Button(root, text="=", command=cmd, width=7,
                  pady="1", bg="gray").grid(row=9, column=3)

"Создаем поле для ввода/вывода данных"

calc_entry = tk.Entry(root, width=50)
calc_entry.grid(row=0, column=0, columnspan=5)
calc_entry1 = tk.Entry(root, width=50, bg="sky blue", fg="black")
calc_entry1.grid(row=1, column=0, columnspan=5)
calc_entry2 = tk.Entry(root, width=50, bg="sky blue", fg="black")
calc_entry2.grid(row=2, column=0, columnspan=5)

"""Завершаем работу и зацикливаем приложение"""
root.mainloop()