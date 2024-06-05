import sqlite3
import datetime

#get the current datetime and store it in a variable
currentDateTime  = datetime.datetime.now()
print(currentDateTime)
#make the database connection with detect_types
#def connect_purchases():

connection = sqlite3.connect('Customerpurchases.db',detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)	
cursor = connection.cursor()

#create table in database
#createTable = '''CREATE TABLE GOODS(
			#Customerid INTEGER,
			#CustomerName VARCHAR(100),
			#CustomerPhoneNumber INTEGER,
			#CustomerDOS TIMESTAMP);'''
#cursor.execute(createTable)
#print("Table created successfully...")
#connection.commit()
#cursor.close()
#connection()

#create Query to insert the data
def add_purchase(Customerid,CustomerName,CustomerPhoneNumber,CustomerDOS):
	cotex = sqlite3.connect('Customerpurchases.db',detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)	
	cure = cotex.cursor()

	insertQuery = "INSERT INTO GOODS VALUES (?,?,?,?)",(Customerid,CustomerName,CustomerPhoneNumber,CustomerDOS)
	#data_tuple = (Customerid,CustomerName,CustomerPhoneNumber,CustomerDOS)	
	#insert the data into table
	cure.execute(str(insertQuery))
	print("Date inserted successfully...")
	cotex.commit()
	cure.close()
	cotex.close  ()

#connect_purchases()
#add_purchase()