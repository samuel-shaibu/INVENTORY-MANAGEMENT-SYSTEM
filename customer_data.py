import sqlite3

def connect():
    conn=sqlite3.connect("customerdata.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS customerdata (id INTEGER PRIMARY KEY, customername text,customerphonenumber INTEGER, Dos text)")
    conn.commit()
    conn.close()
	#print('table created successfully...')

def insert(customername,customerphonenumber,dos):
    conn=sqlite3.connect("customerdata.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO customerdata VALUES (NULL,?,?,?)",(customername,customerphonenumber,dos))
    conn.commit()
    conn.close()
    #view()
	#print("inserted successfull...")

def view():
    conn=sqlite3.connect("customerdata.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM customerdata")
    rows=cur.fetchall()
    conn.close()
    return rows

def delf(id):
    conn=sqlite3.connect("customerdata.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM customerdata WHERE id=?",(id,))
    conn.commit()
    conn.close()
connect()
#insert()
#view()
