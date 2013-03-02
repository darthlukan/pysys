import sys
from tkinter import *


class HelloClass:
    """
        Merging examples.
    """
    def __init__(self):
        quitter = Button(None, text='Hello event world', command=self.quit)
        quitter.pack()
        caller = Button(None, text='This is crazy', command=self.__call__)
        caller.pack()

        self.msg = 'Call me maybe?'

    def quit(self):
        print('hello class method world')
        sys.exit()

    def __call__(self):
        print(self.msg)

HelloClass()
mainloop()