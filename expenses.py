import sqlite3

def daily_expenses():
	conn = sqlite3.connect("expenses.db")
	cur= conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS daily_expenses(id INTEGER PRIMARY KEY,expenses_name text,quantity int,price int,doe text)")
	conn.commit()
	conn.close()
	print("table created successfully...")

def add_expenses(expenses_name,quantity,price,doe):
	conn = sqlite3.connect("expenses.db")
	cur = conn.cursor()
	cur.execute("INSERT INTO daily_expenses VALUES(NULL,?,?,?,?)",(expenses_name,quantity,price,doe))
	conn.commit()
	conn.close()
	print("inserted successfully...")

def view_expenses():
	conn = sqlite3.connect("expenses.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM daily_expenses")
	rows = cur.fetchall()
	conn.close()
	#print(rows)
	return rows

daily_expenses()
#add_expenses("fuelling generator","3kg gallon", 3000,22-1-2022)
#view_expenses()