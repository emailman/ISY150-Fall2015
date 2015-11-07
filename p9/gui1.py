from tkinter import *

__author__ = 'emailman'


def main():
    # Create a window
    window = Tk()

    # Create a label
    label = Label(window, text='Hello World')

    # Put the label in the window on the left side
    label.pack(side=LEFT)

    window.mainloop()


main()
