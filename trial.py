# import tkinter as tk
from argparse import Action
from cgitb import text
from ctypes import alignment
from tkinter import *

# root = tk.Tk()
root = Tk()

# WINDOW PARAMETERS
# root.minsize(600,400)
root.geometry("600x400")
root.title("Number System Converter")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

# INPUT LABELS
l1 = Label(text="Input")
l2 = Label(text="Output")
l1.grid(row=0, column=0, columnspan=2, sticky="nswe")
l2.grid(row=0, column=2, columnspan=2, sticky="nswe")

# INPUT FIELDS
e1 = Entry(root)
e2 = Entry(root)
e1.insert(0, '0000')
e2.insert(0, '0000')
e1.grid(row=1, column=0, columnspan=2, sticky="nswe")
e2.grid(row=1, column=2, columnspan=2, sticky="nswe")
e2.config(state=DISABLED)

# DROPDOWNS FOR BASES
baselist1 = ['Binary', 'Octal', 'Decimal', 'Hexadecimal']
baselist2 = ['Binary', 'Octal', 'Decimal', 'Hexadecimal']
value1 = StringVar()
value1.set(baselist1[3])
value2 = StringVar()
value2.set(baselist2[3])
obase = OptionMenu(root, value1, *baselist1)
obase.grid(row=3, column=0)
dbase = OptionMenu(root, value2, *baselist2)
dbase.grid(row=3, column=1)

# CONVERT BUTTON
def buttonhandler():
    print("Pressed")
b = Button(root, text="CONVERT", command=buttonhandler)
b.grid(row=3, column=2, columnspan=2)

root.mainloop()