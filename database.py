import sqlite3
#Query the DB and Return all records
def show_all():
	#connect to database
	conn = sqlite3.connect('nascomsoft embedded management system')

	#create a cursor
	c = conn.cursor()
	# Query the database
	c.execute("SELECT rowid, *FROM customers")
	items = c.fetchall()

	for item in items:
		print(item)
	print("command executed successfully....")

	conn.commit()

	#close our connection
	conn.close()
 
#Add a New Record To the Table
def add_many(list):
 	conn = sqlite3.connect('nascomsoft embedded management system')
 	c = conn.cursor()
 	c.executemany("INSERT INTO customers VALUES(?,?,?)",(list))
 	conn.commit()
 	#close our connection
 	conn.close()

#Delete Record from table
def delete_one(id):
	conn = sqlite3.connect('nascomsoft embedded management system')
	c = conn.cursor()
	c.execute("DELETE from customers WHERE rowid = (?)",id)
	conn.commit()
	#close our connection
	conn.close()

#Lookup with where
def email_lookup(email):
	conn = sqlite3.connect('nascomsoft embedded management system')
	c = conn.cursor()
	c.execute("SELECT rowid, * from customers WHERE email = (?)", (email,))
	items = c.fetchall()

	for item in items:
		print(item)
	conn.commit()
	#close our connection
	conn.close()
#