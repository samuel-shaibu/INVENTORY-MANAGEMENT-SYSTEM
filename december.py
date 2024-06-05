import sqlite3

def december_connected():
    conn=sqlite3.connect("dec_connect.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS dec_connect (id INTEGER PRIMARY KEY, itemname text,itemprice int,itemQuantity int,itemdos text)")
    conn.commit()
    conn.close()
    print("Connection created successfully...")


def december_insert(name,prize,quantity,dos):
    conn=sqlite3.connect("dec_connect.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO dec_connect VALUES (NULL,?,?,?,?)",(name,prize,quantity,dos))
    conn.commit()
    conn.close()
    #view()
    print('december_insert keyword is working so please move on...')

def december_exhibit():
    conn=sqlite3.connect("dec_connect.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM dec_connect")
    rows=cur.fetchall()
    conn.close()
    return rows

def dec_delete(id):
    conn=sqlite3.connect("dec_connect.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM dec_connect WHERE id=?",(id,))
    conn.commit()
    conn.close()
    print('deleted successfully...')

#how to combine and measure the amount of rows in a table
december_connected()
#december_exhibit()
#dec_delete(1)
