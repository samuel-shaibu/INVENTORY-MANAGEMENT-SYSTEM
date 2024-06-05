import sqlite3

def june_connected():
    conn=sqlite3.connect("jun_connect.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS jun_connect (id INTEGER PRIMARY KEY, itemname text,itemprice int,itemQuantity int,itemdos text)")
    conn.commit()
    conn.close()
    print("Connection created successfully...")


def june_insert(name,prize,quantity,dos):
    conn=sqlite3.connect("jun_connect.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO jun_connect VALUES (NULL,?,?,?,?)",(name,prize,quantity,dos))
    conn.commit()
    conn.close()
    #view()
    print('june_insert keyword is working so please move on...')

def june_exhibit():
    conn=sqlite3.connect("jun_connect.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM jun_connect")
    rows=cur.fetchall()
    conn.close()
    return rows

def jun_delete(id):
    conn=sqlite3.connect("jun_connect.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM jun_connect WHERE id=?",(id,))
    conn.commit()
    conn.close()

#how to combine and measure the amount of rows in a table
june_connected()
#june_exhibit()

