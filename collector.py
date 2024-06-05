import sqlite3
# this is the database and file that contains the view,add, and update functions
def connect():
    conn=sqlite3.connect("commodity.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS commodity (id INTEGER PRIMARY KEY, commodityname text, commodityprice integer, commodityquantity integer)")
    conn.commit()
    conn.close()
    print("table and connection created successfully...")

def display():
    conn=sqlite3.connect("commodity.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM commodity")
    rows=cur.fetchall()
    conn.close()
    return rows
    print("viewing successfully...")

def input(commodityname,commodityprice,commodityquantity):
    conn=sqlite3.connect("commodity.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO commodity VALUES (NULL,?,?,?)",(commodityname,commodityprice,commodityquantity))
    conn.commit()
    conn.close()
    #view()
	#print("inputed successfully...")

def find(commodityname="",commodityprice="",commodityquantity=""):
    conn=sqlite3.connect("commodity.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM commodity WHERE commodityname=? OR commodityprice=? OR commodityquantity=?", (commodityname,commodityprice,commodityquantity))
    rows=cur.fetchall()
    conn.close()
    return rows

def remove(id):
    conn=sqlite3.connect("commodity.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM commodity WHERE id=?",(id,))
    conn.commit()
    conn.close()

def improve(id,commodityname,commodityprice,commodityquantity):
    conn=sqlite3.connect("commodity.db")
    cur=conn.cursor()
    cur.execute("UPDATE commodity SET commodityname=?, commodityprice=?, commodityquantity=? WHERE id=?",(commodityname,commodityprice,commodityquantity,id))
    conn.commit()
    conn.close()

connect()
#display()