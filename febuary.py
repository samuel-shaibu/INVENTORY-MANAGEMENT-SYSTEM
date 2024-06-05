import sqlite3

def febuary_connected():
    conn=sqlite3.connect("feb_connect.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS feb_connect (id INTEGER PRIMARY KEY, itemname text,itemprice int,itemQuantity int,itemdos text)")
    conn.commit()
    conn.close()
    print("Connection created successfully...")


def febuary_insert(name,prize,quantity,dos):
    conn=sqlite3.connect("feb_connect.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO feb_connect VALUES (NULL,?,?,?,?)",(name,prize,quantity,dos))
    conn.commit()
    conn.close()
    #view()
    print('febuary_insert keyword is working so please move on...')

def febuary_exhibit():
    conn=sqlite3.connect("feb_connect.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM feb_connect")
    rows=cur.fetchall()
    conn.close()
    return rows

def feb_delete(id):
    conn=sqlite3.connect("feb_connect.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM feb_connect WHERE id=?",(id,))
    conn.commit()
    conn.close()

#how to combine and measure the amount of rows in a table
febuary_connected()
#febuary_exhibit()

