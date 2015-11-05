__author__ = 'emailman'

import tkinter


def main():
    # Create a window
    main_window = tkinter.Tk()

    # Create a label
    label1 = tkinter.Label(main_window, text='Hello World!')

    # Create a label
    label2 = tkinter.Label(main_window, text="I don't like spam!")

    # Put the label in the window on the left side
    label1.pack(side='top')
    label2.pack(side='top')

    tkinter.mainloop()


main()

