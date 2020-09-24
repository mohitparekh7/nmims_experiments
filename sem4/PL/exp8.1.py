import sqlite3
c = sqlite3.connect("Employee.db")
cr=c.cursor()
def create():
    cr.execute("CREATE TABLE if not exists Employee(e_id integer primary key,e_name text,e_sname text,e_number integer )")
def insert(id,name,sname,phone):
    cr.execute("INSERT into Employee values(?,?,?,?)",(id,name,sname,phone))
    c.commit()
def update():
    cr.execute("UPDATE Employee set e_name ='mohit' where e_sname ='D' ")
    c.commit()
    cr.execute("Select * FROM employee")
    print(cr.fetchall())
def delete():
    cr.execute("DELETE FROM Employee where e_name = 'any' ")
    c.commit()
    print("After deletion :")
    cr.execute("Select * FROM employee")
    print(cr.fetchall())

def retrieve():
    cr.execute("SELECT * FROM Employee")
    print(cr.fetchall())
def retrive_one():
    cr.execute("SELECT * FROM Employee")
    print(cr.fetchone())

create()
for i in range(5):
   insert(input("Employee id: "),input("Employee Name: "),input("Employee Surname: "),input("Employee Phone number: "))
#retrieve()
#retrive_one()
#update()
#delete()
