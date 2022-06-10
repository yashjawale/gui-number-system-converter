import tkinter

window = tkinter.Tk()

window.title("Hello GUI!")
window.minsize(width=500, height=300)
#  for generating a screen

# window immediately crashes

my_label = tkinter.Label(text="Hello", font=("Arial", 24, "bold"))
my_label.pack(expand=1)
window.configure(bg='#34ebab')


#34ebcf





window.mainloop()
#  keep the window running for an infinite amount of time keep at end
