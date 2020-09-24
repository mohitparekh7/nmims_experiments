from tkinter import *
t = Tk()

left =Frame(t)
left.pack(side = LEFT)

right = Frame(t)
right.pack(side= RIGHT)

l1 = Label(right,text="Name:").pack()

e1 = Entry(right).pack()
b1 = Button(right,text = "Okay").pack(side =LEFT,padx =10)
b2 = Button(right,text = "Cancel").pack(side =LEFT,padx =10)

e2 = Entry(left).pack(anchor = N , ipadx = 20 , ipady = 30)
c1 = Checkbutton(left,text= "ONE").pack(side = LEFT)
c2 = Checkbutton(left,text= "TWO").pack(side = LEFT)
c3 = Checkbutton(left,text= "THREE").pack(side = LEFT)

t.mainloop()