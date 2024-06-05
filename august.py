import sqlite3

def august_connected():
    conn=sqlite3.connect("aug_connect.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS aug_connect (id INTEGER PRIMARY KEY, itemname text,itemprice int,itemQuantity int,itemdos text)")
    conn.commit()
    conn.close()
    print("Connection created successfully...")


def august_insert(name,prize,quantity,dos):
    conn=sqlite3.connect("aug_connect.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO aug_connect VALUES (NULL,?,?,?,?)",(name,prize,quantity,dos))
    conn.commit()
    conn.close()
    #view()
    print('august_insert keyword is working so please move on...')

def august_exhibit():
    conn=sqlite3.connect("aug_connect.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM aug_connect")
    rows=cur.fetchall()
    conn.close()
    return rows

def aug_delete(id):
    conn=sqlite3.connect("aug_connect.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM aug_connect WHERE id=?",(id,))
    conn.commit()
    conn.close()
#how to combine and measure the amount of rows in a table
august_connected()
#august_exhibit()

