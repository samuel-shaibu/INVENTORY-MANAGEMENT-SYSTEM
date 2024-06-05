import sqlite3

def september_connected():
    conn=sqlite3.connect("sept_connect.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS sept_connect (id INTEGER PRIMARY KEY, itemname text,itemprice int,itemQuantity int,itemdos text)")
    conn.commit()
    conn.close()
    print("Connection created successfully#...")


def september_insert(name,prize,quantity,dos):
    conn=sqlite3.connect("sept_connect.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO sept_connect VALUES (NULL,?,?,?,?)",(name,prize,quantity,dos))
    conn.commit()
    conn.close()
    #view()
    print('september_insert keyword is working so please move on...')

def september_exhibit():
    conn=sqlite3.connect("sept_connect.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM sept_connect")
    rows=cur.fetchall()
    conn.close()
    return rows

def sept_delete(id):
    conn=sqlite3.connect("sept_connect.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM sept_connect WHERE id=?",(id,))
    conn.commit()
    conn.close()

#how to combine and measure the amount of rows in a table
september_connected()
#september_exhibit()

