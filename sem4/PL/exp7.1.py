from  tkinter import *
t= Tk()

top = Frame(t)
top.pack()


bottom = Frame(t)
bottom.pack(side = BOTTOM)

t.title("a simple gui")

l1=Label(top,text="This is our first gui")
l1.pack()

b1=Button(t,text="Greet")
b2=Button(bottom,text="Close")

b1.pack()
b2.pack()

t.mainloop()

