from tkinter import *
import tkinter.messagebox

__author__ = 'emailman'

# Using tkinter radio buttons and check boxes

# Define the radio button variables
rb_sandwich_var = IntVar
rb_bread_var = IntVar

# Define the checkbox variables
cb_ketchup_var = IntVar
cb_mayo_var = IntVar
cb_mustard_var = IntVar


def main():
    # Create a window
    window = Tk()
    window.title("Jimmy John's Sandwich Order Screen")

    # Put labels in the first row
    lb_sandwich = Label(window, text="Sandwich", font=("Helvitica", 16))
    lb_sandwich.grid(row=0, column=0, padx="20", pady="5", sticky='W')

    lb_bread = Label(window, text="Bread", font=("Helvitica", 16))
    lb_bread.grid(row=0, column=1, padx="20", pady="5", sticky='W')

    lb_condiment = Label(window, text="Condiment", font=("Helvitica", 16))
    lb_condiment.grid(row=0, column=2, padx="20", pady="5", sticky='W')

    # Setup the variable for the sandwich radio buttons
    global rb_sandwich_var
    rb_sandwich_var = IntVar()

    # Put the Sandwich radio buttons in the grid in column 0
    rb_ham = Radiobutton(window, text="Ham", font=("Helvitica", 14), variable=rb_sandwich_var, value=1)
    rb_ham.grid(row=1, column=0, sticky='W', padx=20)

    rb_tuna = Radiobutton(window, text="Tuna", font=("Helvitica", 14), variable=rb_sandwich_var, value=2)
    rb_tuna.grid(row=2, column=0, sticky='W', padx=20)

    rb_turkey = Radiobutton(window, text="Turkey", font=("Helvitica", 14), variable=rb_sandwich_var, value=3)
    rb_turkey.grid(row=3, column=0, sticky='W', padx=20)

    # Setup the variable for the bread radio buttons
    global rb_bread_var
    rb_bread_var = IntVar()

    # Bread radio button with value = 1 is the default
    rb_bread_var.set(1)

    # Put the Bread radio buttons in the grid in column 1
    rb_rye = Radiobutton(window, text="Rye", font=("Helvitica", 14), variable=rb_bread_var, value=1)
    rb_rye.grid(row=1, column=1, sticky='W', padx=20)

    rb_wheat = Radiobutton(window, text="Wheat", font=("Helvitica", 14), variable=rb_bread_var, value=2)
    rb_wheat.grid(row=2, column=1, sticky='W', padx=20)

    rb_white = Radiobutton(window, text="White", font=("Helvitica", 14), variable=rb_bread_var, value=3)
    rb_white.grid(row=3, column=1, sticky='W', padx=20)

    # Setup the variables for the condiment check boxes
    global cb_ketchup_var
    cb_ketchup_var = IntVar()

    global cb_mustard_var
    cb_mustard_var = IntVar()

    global cb_mayo_var
    cb_mayo_var = IntVar()

    # Put the Condiment check boxes in the grid in column 2
    cb_ketchup = Checkbutton(window, text="Ketchup", font=("Helvitica", 14), variable=cb_ketchup_var)
    cb_ketchup.grid(row=1, column=2, sticky='W', padx=20)

    cb_mayo = Checkbutton(window, text="Mayonnaise", font=("Helvitica", 14), variable=cb_mayo_var)
    cb_mayo.grid(row=2, column=2, sticky='W', padx=20)

    cb_mustard = Checkbutton(window, text="Mustard", font=("Helvitica", 14), variable=cb_mustard_var)
    cb_mustard.grid(row=3, column=2, sticky='W', padx=20)

    # Put three buttons in row 4
    bt_order = Button(window, text="ORDER", font=("Helvitica", 14), command=order)
    bt_order.grid(row=4, column=0, pady=10)

    bt_cancel = Button(window, text="CANCEL", font=("Helvitica", 14), command=cancel)
    bt_cancel.grid(row=4, column=1, pady=10)

    bt_quit = Button(window, text="   QUIT   ", font=("Helvitica", 14), command=window.destroy)
    bt_quit.grid(row=4, column=2, pady=10)

    window.mainloop()


def order():
    tkinter.messagebox.showinfo("Jimmy John's", "You order has been placed")
    clear()


def cancel():
    tkinter.messagebox.showerror("Jimmy John's", "You order has been canceled")
    clear()


def clear():
    rb_bread_var.set(0)
    rb_sandwich_var.set(0)
    cb_ketchup_var.set(0)
    cb_mayo_var.set(0)
    cb_mustard_var.set(0)


main()
