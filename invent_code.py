import sqlite3

#connect to the database
def connect_todatabase_():
    kon = sqlite3.connect('INVENTORY SYSTEM')
    #create a cursor
    k = kon.cursor()
    k.execute("CREATE TABLE IF NOT EXIST items(id INTEGER PRIMARY KEY,name text,prize int,Quantity int)")
    print("table created successfully")
    kon.commit()
    #close our connection
    kon.close()    


# commit our connection


def show_all():
    kon = sqlite3.connect('INVENTORY SYSTEM')
    k = kon.cursor()
    k.execute("SELECT rowid, * from items")
    #declaring a variable
    info = k.fetchall()
    # commit our connection
    kon.commit()
    #close our connection
    return info

# Add item to the database
def add(name,prize,Quantity):
    kon = sqlite3.connect('INVENTORY SYSTEM')
    k = kon.cursor()
    k.execute("INSERT INTO items VALUES (?, ?, ?)", (name,prize,Quantity))
    # commit our connection
    kon.commit()
    #close our connection
    kon.close()

# To search for items in the database
def search(name ="",prize="",Quantity=""):
    kon = sqlite3.connect('INVENTORY SYSTEM')
    k = kon.cursor()
    k.execute("SELECT rowid, * FROM items WHERE name = ? OR prize = ? OR Quantity = ?",(name,prize,Quantity))
    rows = k.fetchall()
    #commit our connection
    kon.commit()
    #close our connection
    kon.close()
    return rows

#To delete a table or item from database
def delete(name):
     kon = sqlite3.connect('INVENTORY SYSTEM')
     k = kon.cursor()
     k.execute("DELETE from items WHERE name = ?",(name,))
     kon.commit()
     kon.close()
# how can i connect two tables together in sqlite3 python?

# To update the prize and quantity of my items
def update(name,prize,Quantity):
    kon = sqlite3.connect('INVENTORY SYSTEM')
    k = kon.cursor()
    k.execute("UPDATE items SET name = ?,prize = ? WHERE Quantity = ?",(name,prize,Quantity))
    #commit our connection
    kon.commit()
    #close our connection
    kon.close()


#connect_todatabase_()
#show_all()
#search()
#add(name,prize,Quantity)
#purchases()
#customer_info()
#add_customer()
#update()
#view_purchases()