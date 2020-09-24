from  tkinter import *
t= Tk()

t.title("Select a bank")
v =StringVar(t,0)

def p():
    print(v.get())

l1=Label(t,
        text="""Choose a bank:""",
        justify = LEFT,
        padx = 20).pack()

b1=Radiobutton(t,
              text="SBI",
              padx = 20,
              variable=v,
              value="SBI",command = p).pack(anchor=W)

b2=Radiobutton(t,
              text="HDFC",
              padx = 20,
              variable=v,
              value="HDFC",command = p).pack(anchor=W)

b3=Radiobutton(t,
              text="ICICI",
              padx = 20,
              variable=v,
              value="ICICI",command = p).pack(anchor=W)

b4=Radiobutton(t,
              text="CBI",
              padx = 20,
              variable=v,
              value="CBI",command = p).pack(anchor=W)

b5=Radiobutton(t,
              text="BOI",
              padx = 20,
              variable=v,
              value="BOI",command = p).pack(anchor=W)



t.mainloop()

