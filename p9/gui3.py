__author__ = 'emailman'

import tkinter
import tkinter.messagebox


def main():
    # Create a window
    main_window = tkinter.Tk()

    # Create a label
    label1 = tkinter.Label(main_window, text='Hello World!')

    # Create a label
    label2 = tkinter.Label(main_window, text="I don't like spam!")

    # Create a button
    my_button = tkinter.Button(main_window, text='Click Me', command=do_something)

    # Put the label in the window on the left side
    label1.pack(side='top')
    label2.pack(side='top')
    my_button.pack(side='top')

    tkinter.mainloop()


def do_something():
    tkinter.messagebox.showinfo("Message Box", "You clicked the button")


main()
