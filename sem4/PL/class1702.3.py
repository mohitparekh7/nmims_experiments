import sqlite3

from tkinter import *
t=Tk()

l1=Label(t,text="Username:")
l1.grid(row=0,column=0)
entry1=Entry(t)
entry1.grid(row=0,column=1)
l2=Label(t,text="Password:")
l2.grid(row=1,column=0)
entry2=Entry(t)
entry2.grid(row=1,column=1)
l3=Label(t,text="Contact:")
l3.grid(row=2,column=0)
entry3=Entry(t)
entry3.grid(row=2,column=1)
l4=Label(t,text="Email:")
l4.grid(row=3,column=0)
entry4=Entry(t)
entry4.grid(row=3,column=1)


connection = sqlite3.connect('login.db')
cursor= connection.cursor()

def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS login(username TEXT,password TEXT,email Text, phnumber REAL)')
    cursor.execute("INSERT INTO login VALUES (?,?,?,?)",(entry1.get(),entry2.get(),entry3.get(),entry4.get()))
    connection.commit()
    cursor.close()
    connection.close()
'''
def reading():
    cursor.execute('SELECT * FROM company')
    #data = cursor.fetchall()
    #print(data)
    for row in cursor.fetchall():
        print(row)
'''
b=Button(t,text='LOGIN',command=create_table)
b.grid(row=4,column=1)
t.mainloop()
