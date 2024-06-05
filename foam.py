import sqlite3

def connected():
    conn=sqlite3.connect("monthly_sales.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE monthly_sales (id PRIMARY kEY, itemname text,itemprice int,itemQuantity int,itemdos text)")
    conn.commit()
    conn.close()
    print("Connection created successfully...")


def december(name,prize,quantity,dos):
    conn=sqlite3.connect("monthly_sales.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO monthly_sales VALUES (NULL,?,?,?,?)",(name,prize,quantity,dos))
    conn.commit()
    conn.close()
    #view()
    print('foam reinsert keyword is working so please move on...')

def exhibit():
    conn=sqlite3.connect("monthly_sales.db")
    cur=conn.cursor()
    cur.execute("SELECT rowid ,* FROM monthly_sales")
    rows=cur.fetchall()
    conn.close()
    print(rows)

#how to combine and measure the amount of rows in a table
#connected()
exhibit()