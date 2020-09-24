"""
from tkinter import *

import tkinter.messagebox #importing message box or dialog box

t = Tk()

tkinter.messagebox.showinfo("message box(title)","do you want to exit")
t.mainloop()

"""
"""
from tkinter import *

import tkinter.messagebox #importing message box or dialog box

t = Tk()


ans = tkinter.messagebox.askquestion("Question","do you want to exit ?")
if ans =='yes':
    print("yes want to exit")
t.mainloop()

"""

"""

from tkinter import *

t = Tk()
canvas = Canvas(t,width=300,height=300)
canvas.pack()
line = canvas.create_line(0,0,200,40)
line1=canvas.create_line(0,100,200,40, fill ='blue')
box = canvas.create_rectangle(20,20,100,50, fill = 'green')
t.mainloop()

"""
"""

from tkinter import *
t=Tk()

statusbar=Label(t,text="saving the file",bd = 1 , relief=SUNKEN,anchor=W)

statusbar.pack(side=BOTTOM,fill = X)
t.mainloop()

"""