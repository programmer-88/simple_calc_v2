#!/usr/bin/python3
from engine.funcs import *
from tkinter import *
from engine.printer import *


window = Tk()

b1 = Button(window, text="execute", command = arithmetic_check)
b1.grid(row = 0, column = 0)

en_in_1 = StringVar()
en1 = Entry(window, textvariable = en_in_1)
en1.grid(row = 0, column =1)

t_out_1 = Text(window, height =1, width = 40)
t_out_1.grid(row = 1, column = 0, columnspan = 2)

window.mainloop()
