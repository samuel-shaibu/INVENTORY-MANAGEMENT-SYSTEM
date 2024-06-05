import sqlite3

def connect():
    conn=sqlite3.connect("stores.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE stores (id INTEGER PRIMARY KEY, CREATE TABLE IF NOT EXIST purchases(id INTEGER PRIMARY KEY,name text,prize int,Quantity int,dos text)")
    conn.commit()
    conn.close()
    print("Connection created successfully...")


def insert(name,prize,quantity,dos):
    conn=sqlite3.connect("stores.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO stores VALUES (NULL,?,?,?,?)",(name,prize,quantity,dos))
    conn.commit()
    conn.close()
    #view()

connect()