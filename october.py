import sqlite3

def october_connected():
    conn=sqlite3.connect("oct_connect.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS oct_connect (id INTEGER PRIMARY KEY, itemname text,itemprice int,itemQuantity int,itemdos text)")
    conn.commit()
    conn.close()
    print("Connection created successfully...")


def october_insert(name,prize,quantity,dos):
    conn=sqlite3.connect("oct_connect.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO oct_connect VALUES (NULL,?,?,?,?)",(name,prize,quantity,dos))
    conn.commit()
    conn.close()
    #view()
    print('october_insert keyword is working so please move on...')

def october_exhibit():
    conn=sqlite3.connect("oct_connect.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM oct_connect")
    rows=cur.fetchall()
    conn.close()
    return rows

def oct_delete(id):
    conn=sqlite3.connect("oct_connect.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM oct_connect WHERE id=?",(id,))
    conn.commit()
    conn.close()

#how to combine and measure the amount of rows in a table
october_connected()
#october_exhibit()
