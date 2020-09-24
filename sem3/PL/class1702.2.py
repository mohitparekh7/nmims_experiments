"""
import sqlite3

connection = sqlite3.connect('company.db')
cursor= connection.cursor()

def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS company(name TEXT,surname TEXT, number REAL)')

def data_entries():
    cursor.execute("INSERT INTO company VALUES ('a','b','9856')")
    connection.commit()
    cursor.close()
    connection.close()

def reading():
    cursor.execute('SELECT * FROM company')
    #data = cursor.fetchall()
    #print(data)
    for row in cursor.fetchall():
        print(row)


#create_table()
#data_entries()
reading()


"""