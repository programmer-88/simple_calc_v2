#!/usr/bin/python3
from engine.funcs import *
from tkinter import *
from engine.printer import *

def exec_func():
    t_out_1.delete(1.0, "end")
    result = arithmetic_check(en_in_1.get())
    t_out_1.insert(END, result)

window = Tk()
window.title("Calc_v2")

en_in_1 = StringVar()

en1 = Entry(window, textvariable = en_in_1)
en1.grid(row = 0, column =1)

b1 = Button(window, text="execute", command = exec_func)
b1.grid(row = 0, column = 0)

t_out_1 = Text(window, height =1, width = 40)
t_out_1.grid(row = 1, column = 0, columnspan = 2)

window.mainloop()
