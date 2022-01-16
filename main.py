from tkinter import *

root = Tk()
root.geometry("1920x1080")

# TODO Make it so you can set preferences
# TODO Make the texts that you are attempting to input auto generate


def set_screen():
    global screenElem
    screenElem = [
        Label(root, text=""),
        Entry(root)
    ]
    set_grid()


def set_grid():
    screenElem[0].grid(row=0, column=0)
    screenElem[1].grid(row=1, column=0)


root.title("Programming GWAM")
set_screen()

root.mainloop()