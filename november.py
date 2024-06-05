import sqlite3

def november_connected():
    conn=sqlite3.connect("nov_connect.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS nov_connect (id INTEGER PRIMARY KEY, itemname text,itemprice int,itemQuantity int,itemdos text)")
    conn.commit()
    conn.close()
    print("Connection created successfully#...")


def november_insert(name,prize,quantity,dos):
    conn=sqlite3.connect("nov_connect.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO nov_connect VALUES (NULL,?,?,?,?)",(name,prize,quantity,dos))
    conn.commit()
    conn.close()
    #view()
    print('november_insert keyword is working so please move on...')

def november_exhibit():
    conn=sqlite3.connect("nov_connect.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM nov_connect")
    rows=cur.fetchall()
    conn.close()
    return rows

def nov_delete(id):
    conn=sqlite3.connect("nov_connect.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM nov_connect WHERE id=?",(id,))
    conn.commit()
    conn.close()

#how to combine and measure the amount of rows in a table
november_connected()
#november_exhibit()
