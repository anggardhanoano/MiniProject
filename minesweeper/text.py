from tkinter import *

color="red"
default_color="white"

def main(n=10):
    window = Tk()
    last_clicked = [None]
    for x in range(n):
        for y in range(n):
            b = Button(window, bg=default_color, activebackground=default_color)
            b.grid(column=x, row=y)
            # creating the callback with "b" as the default parameter bellow "freezes" its value pointing
            # to the button created in each run of the loop.
            b["command"] = lambda b=b: click(b, last_clicked)
    return window

def click(button, last_clicked):
    if last_clicked[0]:
        last_clicked[0]["bg"] = default_color
        last_clicked[0]["activebackground"] = default_color
    button["bg"] = color
    button["activebackground"] = color
    last_clicked[0] = button

w = main()
window.mainloop()
