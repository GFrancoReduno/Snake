from customtkinter import CTk, CTkButton, CTkEntry
from tkinter import StringVar, PhotoImage
import customtkinter as ct


class CirclularButton(CTkButton):
    def __init__(self, master=None, text='', command=None):
        super().__init__(master = master, text= text, command= command)
        self.configure(width = 50, height= 70, corner_radius=20,
        hover_color= ('#cccccc', '#333333'),
            fg_color = ('#7f5af0', '#7f5af0'),
            text_font = ('firacode', 16))
        self.grid(padx=5, pady=5,sticky= 'nsew')

def toggle_mode():
    pass

root = CTk()
root.geometry('375x500')
root.title('')
root.resizable(False, False)
root.call('wm', 'iconphoto', root._w, PhotoImage(file = 'images/logo.png'))
root.configure(bg = "black")
ct.set_appearance_mode("Dark")

mode = 'dark'
expression = StringVar()
img_light = PhotoImage(file= 'images/sun.png')
img_dark = PhotoImage(file = 'images/moon.png')

button_mode = CTkButton(root, image = img_light, text='',
    hover_color=('white', 'black'),
    fg_color = ('white', 'black'), width=50, height=50,
    command = toggle_mode)
button_mode.grid(row=0, column= 0)

entry= CTkEntry(root, textvariable = expression,
    text_font = ('Helvetica', 28), justify = 'right',
    text_color = ("black", "white"),
    corner_radius = 0, state ="disabled",
    width= 280, fg_color = ("white", "black"), border= 0)
entry.grid(row=0, column=1, columspan=3, padx=5, ipady=15, pady=10)

CirclularButton(root, text= ' C ',).grid(row=1, column=0)
CirclularButton(root, text= '+/-',).grid(row=1, column=1)
CirclularButton(root, text= ' % ',).grid(row=1, column=2)
CirclularButton(root, text= ' ÷ ',).grid(row=1, column=3)

CirclularButton(root, text= '7',).grid(row=2, column=0)
CirclularButton(root, text= '8',).grid(row=2, column=1)
CirclularButton(root, text= '9',).grid(row=2, column=2)
CirclularButton(root, text= 'x',).grid(row=2, column=3)

CirclularButton(root, text= '4',).grid(row=3, column=0)
CirclularButton(root, text= '5',).grid(row=3, column=1)
CirclularButton(root, text= '6',).grid(row=3, column=2)
CirclularButton(root, text= '-',).grid(row=3, column=3)

CirclularButton(root, text= '1',).grid(row=4, column=0)
CirclularButton(root, text= '2',).grid(row=4, column=1)
CirclularButton(root, text= '3',).grid(row=4, column=2)
CirclularButton(root, text= '+',).grid(row=4, column=3)

CirclularButton(root, text= '0',).grid(row=5, column=0)
CirclularButton(root, text= '.',).grid(row=5, column=1)
CirclularButton(root, text= 'AC',).grid(row=5, column=2)
CirclularButton(root, text= '=',).grid(row=5, column=3)






root.mainloop()