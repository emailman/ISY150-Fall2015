__author__ = 'emailman'

import tkinter


def main():
    # Create a window
    main_window = tkinter.Tk()

    # Create a label
    label = tkinter.Label(main_window, text='Hello World')

    # Put the label in the window on the left side
    label.pack(side='left')

    tkinter.mainloop()


main()
