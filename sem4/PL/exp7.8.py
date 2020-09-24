from tkinter import *
t = Tk()

t.title("Image View")
img = PhotoImage(file="mohit.png")
l = Label(t,image=img)
l.pack()
t.mainloop()