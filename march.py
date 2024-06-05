import sqlite3

def march_connected():
    conn=sqlite3.connect("mar_connect.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS mar_connect (id INTEGER PRIMARY KEY, itemname text,itemprice int,itemQuantity int,itemdos text)")
    conn.commit()
    conn.close()
    print("Connection created successfully...")


def march_insert(name,prize,quantity,dos):
    conn=sqlite3.connect("mar_connect.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO mar_connect VALUES (NULL,?,?,?,?)",(name,prize,quantity,dos))
    conn.commit()
    conn.close()
    #view()
    print('march_insert keyword is working so please move on...')

def march_exhibit():
    conn=sqlite3.connect("mar_connect.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM mar_connect")
    rows=cur.fetchall()
    conn.close()
    return rows

def mar_delete(id):
    conn=sqlite3.connect("mar_connect.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM mar_connect WHERE id=?",(id,))
    conn.commit()
    conn.close()

#how to combine and measure the amount of rows in a table
march_connected()
#march_exhibit()

