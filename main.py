# import tkinter as tk
from tkinter import *
import pyglet

from logic import *

root = Tk()

# WINDOW PARAMETERS
root.geometry("600x300")
root.title("Number System Converter")
root.config(bg="#454545", padx=20, pady=20)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

pyglet.font.add_file('Seven Segment.ttf')
# INPUT LABELS
l1 = Label(text="Input")
l1.config(font=('default', 10), fg="#fff", bg="#454545")
l2 = Label(text="Output")
l2.config(font=('default', 10), fg="#fff", bg="#454545")
l1.grid(row=0, column=0, columnspan=2, sticky="nsw", pady=10)
l2.grid(row=0, column=2, columnspan=2, sticky="nsw", pady=10)

# INPUT FIELDS
e1 = Entry(root)
def setoutput(text):
    e2.configure(state='normal')
    e2.delete(0, END)
    e2.insert(0, str(text))
    e2.configure(state='disabled')
e2 = Entry(root)
e1.config(font=('Seven Segment', 30), fg="#ff7f7f", bg="#521b0a", insertbackground="#ff7f7f")
e2.config(font=('Seven Segment', 30), disabledforeground="#ff7f7f", disabledbackground="#521b0a",fg="#ff7f7f", bg="#521b0a", insertbackground="#ff7f7f")
e1.insert(0, '0000')
# e2.insert(0, '0000')
e1.grid(row=1, column=0, columnspan=2, sticky="nsw")
e2.grid(row=1, column=2, columnspan=2, sticky="nsw")
# e2.config(state=DISABLED)
setoutput("0000")

# DROPDOWNS FOR BASES
# Labels
l3 = Label(text="From:", fg="#fff", bg="#454545")
l4 = Label(text="To:", fg="#fff", bg="#454545")
l3.grid(row=2, column=0, sticky="nsw", pady=(20, 10))
l4.grid(row=2, column=1, sticky="nsw", pady=(20, 10))
baselist1 = ['Binary', 'Octal', 'Decimal', 'Hexadecimal']
baselist2 = ['Binary', 'Octal', 'Decimal', 'Hexadecimal']
value1 = StringVar()
value1.set(baselist1[2])
value2 = StringVar()
value2.set(baselist2[2])
obase = OptionMenu(root, value1, *baselist1)
obase.grid(row=3, column=0, sticky="nsw")
obase.config(fg="#fff", bg="#454545", width=12, highlightbackground="#303030", activebackground="#858585")
obase['menu'].config(bg="#454545", fg="#fff", )
dbase = OptionMenu(root, value2, *baselist2)
dbase.grid(row=3, column=1, sticky="nsw")
dbase.config(fg="#fff", bg="#454545", width=12, highlightbackground="#303030", activebackground="#858585")
dbase['menu'].config(bg="#454545", fg="#fff", )

# BUTTON FUNCTION
def buttonhandler():
    num = e1.get()
    frombase = getbase(value1.get())
    tobase = getbase(value2.get())
    answer = convert(num, frombase, tobase)
    setoutput(answer)

# CONVERT BUTTON
b = Button(root, text="CONVERT", command=lambda: buttonhandler())
b.config(fg="#fff", bg="#454545", padx=4, pady=4, activebackground="#858585")
b.grid(row=3, column=2, columnspan=2)

root.mainloop()