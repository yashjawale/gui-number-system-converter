from tkinter import *
from one import convert

LABEL_PADY = 20
LABEL_PADX = 5
ENTRY_BAR_WIDTH = 20


def calculate():
    ans = convert(num=num_inp.get(), frombase=int(old_base_inp.get()), tobase=int(new_base_inp.get()))
    solution.config(text=ans)
    return ans


window = Tk()

window.title("GUI Number System")
window.config(padx=25, pady=10)
window.minsize(width=500, height=300)


title_label = Label()
title_label.config(text="Number System Converter", font=("Arial", 24, "bold"), padx=25, pady=25, fg="#bb43bf")
title_label.grid(row=0, column=2)


number = Label()
number.config(text="Number", fg="#43bfdd")
number.grid(row=2, column=0, pady=LABEL_PADY, padx=LABEL_PADX)
num_inp = Entry()
num_inp.config(width=ENTRY_BAR_WIDTH)
num_inp.grid(row=2, column=1)
num_inp.focus()


old_base_label = Label()
old_base_label.config(text="Old Base", fg="#43bfdd")
old_base_label.grid(row=2, column=3, pady=LABEL_PADY, padx=LABEL_PADX)
old_base_inp = Entry()
old_base_inp.config(width=ENTRY_BAR_WIDTH)
old_base_inp.grid(row=2, column=4)


new_base_label = Label()
new_base_label.config(text="New Base", fg="#43bfdd")
new_base_label.grid(row=3, column=3, padx=LABEL_PADX)
new_base_inp = Entry()
new_base_inp.config(width=ENTRY_BAR_WIDTH)
new_base_inp.grid(row=3, column=4)


button = Button()
button.config(text="Calculate", command=calculate)
button.grid(row=4, column=2)


answer = Label()
answer.config(text="Answer", fg="#43bfdd")
answer.grid(row=3, column=0, padx=LABEL_PADX)
solution = Label()
solution.grid(row=3, column=1, padx=LABEL_PADX)

window.mainloop()
