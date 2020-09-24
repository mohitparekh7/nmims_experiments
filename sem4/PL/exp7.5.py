from  tkinter import *
t =Tk()
class calling:
    def __init__(self,t):
       self.t = t
       entry = Entry(self.t)
       self.entry = entry
    def greet(self):
        print(self.entry.get())
    def gui(self):
        self.entry.pack()
        b1 = Button(self.t,text="SUBMIT",command=self.greet)
        b1.pack()
        self.t.mainloop()
n =calling(t)
n.gui()