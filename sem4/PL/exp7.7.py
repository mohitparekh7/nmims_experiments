from tkinter import *
t = Tk()

def msg():
    print("New Project Created")

m=Menu(t)
t.config(menu=m)
f=Menu(m)
e=Menu(m)
m.add_cascade(label="FILE",menu=f)
m.add_cascade(label="EDIT",menu=e)
f.add_command(label="New File")
f.add_command(label="New Project",command=msg)
f.add_separator()
f.add_command(label="Quit")
e.add_cascade(label="CUT")
e.add_cascade(label="COPY")
e.add_separator()
e.add_cascade(label="Paste")
t.mainloop()
