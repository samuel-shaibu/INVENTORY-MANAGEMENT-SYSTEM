'''
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 55555))
message = s.recv(1024) 
s.close()

print(message.decode())
'''
 
import sqlite3

class Person:

	def __init__(self, idNumber=-1, first="", last="", age=-1):
		self.idNumber = idNumber
		self.first = first
		self.last = last
		self.age  = age
		self.connection = sqlite3.connect("mydata.db")
		self.cursor = self.connection.cursor()

	def loadPerson(self, idNumber):
		self.cursor.execute("""SELECT * FROM persons 
			WHERE id = []
			""".format(idNumber))

		results = self.cursor.fetchone()

		self.idNumber = idNumber
		self.first = results[1]
		self.last	= results[2]
		self.age =  results[3]

p1 = Person() 
p1.loadPerson(1)
print(p1.first)
print(p1.last)
print(p1.age)
print(p1.idNumber)

# connection = sqlite3.connect("mydata.db")
# cursor = connection.cursor()

# cursor.execute(""" CREATE TABLE IF NOT EXISTS persons 
# 	(	id 	INTEGER PRIMARY KEY,	
# 	firstName  TEXT,
# 	    lastName	TEXT,
# 	    age 	INTEGER	
# 	)""")

# cursor.execute("""INSERT INTO persons VALUES
# ( 'Paul', 'Smith', 24),
# ( 'Mark', 'Johnson', 42),
# ( 'Anna','Smith',34)"""
# )

# cursor.execute("""
# SELECT * FROM persons WHERE lastName = 'Smith' """)

# rows = cursor.fetchall()
# print(rows)



# connection.commit()
# connection.close()