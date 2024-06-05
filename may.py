import sqlite3

def may_connected():
    conn=sqlite3.connect("maye_connect.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS maye_connect (id INTEGER PRIMARY KEY, itemname text,itemprice int,itemQuantity int,itemdos text)")
    conn.commit()
    conn.close()
    print("Connection created successfully...")


def may_insert(name,prize,quantity,dos):
    conn=sqlite3.connect("maye_connect.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO maye_connect VALUES (NULL,?,?,?,?)",(name,prize,quantity,dos))
    conn.commit()
    conn.close()
    #view()
    print('may_insert keyword is working so please move on...')

def may_exhibit():
    conn=sqlite3.connect("maye_connect.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM maye_connect")
    rows=cur.fetchall()
    conn.close()
    return rows

def may_delete(id):
    conn=sqlite3.connect("maye_connect.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM maye_connect WHERE id=?",(id,))
    conn.commit()
    conn.close()

#how to combine and measure the amount of rows in a table
may_connected()
#may_exhibit()

