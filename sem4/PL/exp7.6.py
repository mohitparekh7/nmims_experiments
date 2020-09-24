from tkinter import *
t = Tk()

t1 = Frame(t, bg = "red",highlightcolor="white",highlightthickness=2)
l1 = Label(t1,text = "red",relief = RIDGE,width = 15 ,height = 2)
t1.pack(fill = X)
l1.pack(side = LEFT)

t2 = Frame(t, bg = "green",highlightcolor="white",highlightthickness=2)
l2 = Label(t2,text = "green",relief = RIDGE,width = 15 ,height = 2)
t2.pack(fill = X)
l2.pack(side = LEFT)

t3 = Frame(t, bg = "orange",highlightcolor="white",highlightthickness=2)
l3 = Label(t3,text = "orange",relief = RIDGE,width = 15 ,height = 2)
t3.pack(fill = X)
l3.pack(side = LEFT)

t4 = Frame(t, bg = "white",highlightcolor="white",highlightthickness=2)
l4 = Label(t4,text = "white",relief = RIDGE,width = 15 ,height = 2)
t4.pack(fill = X)
l4.pack(side = LEFT)

t5 = Frame(t, bg = "yellow",highlightcolor="white",highlightthickness=2)
l5 = Label(t5,text = "yellow",relief = RIDGE,width = 15 ,height = 2)
t5.pack(fill = X)
l5.pack(side = LEFT)

t6 = Frame(t, bg = "blue",highlightcolor="white",highlightthickness=2)
l6 = Label(t6,text = "blue",relief = RIDGE,width = 15 ,height = 2)
t6.pack(fill = X)
l6.pack(side = LEFT)


t.mainloop()
