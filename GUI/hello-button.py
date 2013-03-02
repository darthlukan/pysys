#!/usr/bin/python3

from tkinter import *

root = Tk()
Button(root, text='Hello widget world', command=root.quit).pack(side=LEFT)
mainloop()