import sqlite3
#now this database and file is to know the daily sales made

def connect():
    conn=sqlite3.connect("shopped.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE shopped (itemname text,itemprice int,itemQuantity int,itemdos text)")
    conn.commit()
    conn.close()
    print("Connection created successfully...")


def deinsert(itemname,itemprice,itemQuantity,itemdos):
    conn=sqlite3.connect("shopped.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO shopped VALUES (?,?,?,?)",(itemname,itemprice,itemQuantity,itemdos))
    conn.commit()
    conn.close()
    print("item inserted successfully...")
    #view()

def viewed():
    conn=sqlite3.connect("shopped.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM shopped")
    rows=cur.fetchall()
    conn.close()
    return rows

def dry(itemname):
    conn=sqlite3.connect("shopped.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM shopped WHERE itemname=?",(itemname,))
    conn.commit()
    conn.close()    

#connect()
#viewed()