import sqlite3

def july_connected():
    conn=sqlite3.connect("jul_connect.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS jul_connect (id INTEGER PRIMARY KEY, itemname text,itemprice int,itemQuantity int,itemdos text)")
    conn.commit()
    conn.close()
    print("Connection created successfully...")


def july_insert(name,prize,quantity,dos):
    conn=sqlite3.connect("jul_connect.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO jul_connect VALUES (NULL,?,?,?,?)",(name,prize,quantity,dos))
    conn.commit()
    conn.close()
    #view()
    print('july_insert keyword is working so please move on...')

def july_exhibit():
    conn=sqlite3.connect("jul_connect.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM jul_connect")
    rows=cur.fetchall()
    conn.close()
    return rows

def jul_delete(id):
    conn=sqlite3.connect("jul_connect.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM jul_connect WHERE id=?",(id,))
    conn.commit()
    conn.close()

#how to combine and measure the amount of rows in a table
july_connected()
#july_exhibit()

