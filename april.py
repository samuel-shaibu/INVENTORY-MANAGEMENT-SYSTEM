import sqlite3

def april_connected():
    conn=sqlite3.connect("apr_connect.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS apr_connect (id INTEGER PRIMARY KEY, itemname text,itemprice int,itemQuantity int,itemdos text)")
    conn.commit()
    conn.close()
    print("Connection created successfully...")


def april_insert(name,prize,quantity,dos):
    conn=sqlite3.connect("apr_connect.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO apr_connect VALUES (NULL,?,?,?,?)",(name,prize,quantity,dos))
    conn.commit()
    conn.close()
    #view()
    print('april_insert keyword is working so please move on...')

def april_exhibit():
    conn=sqlite3.connect("apr_connect.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM apr_connect")
    rows=cur.fetchall()
    conn.close()
    return rows

def apr_delete(id):
    conn=sqlite3.connect("apr_connect.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM apr_connect WHERE id=?",(id,))
    conn.commit()
    conn.close()

#how to combine and measure the amount of rows in a table
april_connected()
#april_exhibit()

