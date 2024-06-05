import sqlite3

def january_connected():
    conn=sqlite3.connect("jan_connect.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS jan_connect (id INTEGER PRIMARY KEY, itemname text,itemprice int,itemQuantity int,itemdos text)")
    conn.commit()
    conn.close()
    print("Connection created successfully...")


def january_insert(name,prize,quantity,dos):
    conn=sqlite3.connect("jan_connect.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO jan_connect VALUES (NULL,?,?,?,?)",(name,prize,quantity,dos))
    conn.commit()
    conn.close()
    #view()
    print('january_insert keyword is working so please move on...')

def january_exhibit():
    conn=sqlite3.connect("jan_connect.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM jan_connect")
    rows=cur.fetchall()
    conn.close()
    return rows

def jan_delete(id):
    conn=sqlite3.connect("jan_connect.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM jan_connect WHERE id=?",(id,))
    conn.commit()
    conn.close()

#how to combine and measure the amount of rows in a table
january_connected()
#january_exhibit()

