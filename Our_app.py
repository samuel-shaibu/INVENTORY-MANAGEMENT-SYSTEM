#import database
from datetime import datetime
import calendar
from datetime import datetime 
import sqlite3
from tkinter import*
from PIL import ImageTk
import os
import winsound
from tkinter import filedialog

'''
man = Tk()
man.geometry("1255x944")
img =ImageTk.PhotoImage(Image.open("mypicture.jpg"))
labek = Label(image=img)
labek.pack()
man.mainloop()
'''
'''
canvas = Canv as(width = 600,height = 800,bg = 'indigo')
canvas.pack(expand = YES, fill = BOTH)

image = ImageTk.PhotoImage(file = 'Nascomsoft logo3q.jpg')
canvas.create_image(100,10,image = image, anchor=NW)

mainloop()
'''
kot = Tk()
kot.geometry("500x200")

def open_software():
    #print('the current working directory is:',os.path.abspath(__file__))
    #print('Absolute directoryname:',os.path.dirname(os.path.abspath(__file__)))
    #my_software = filedialog.askopenfilename()
    #lab1.config(text = my_software)
    kef = os.system("C:\\sqlite\\sqlitestudio-3.3.3\\SQLiteStudio\\sqlitestudio")
    print('the current working directory is:',kef)
btn1 = Button(kot, bg = 'white', width = 20, height  = 1, command = open_software, text = 'OPEN',bd = 10, padx = 2)
ent1= Entry(kot,width = 15)
ent1.grid()
ent1.focus()
#winsound.Beep(800,460)
#lab1 = Label(kot,text = "")
#lab1.pack()
btn1.grid()
kot.mainloop()
int=num
input = int(num)
print("the number you have inputted is"+num)

'''
def test_connect():
    conn=sqlite3.connect("lang_connect.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE lang_connect (id INTEGER PRIMARY KEY, itemname text,itemprice int,itemQuantity int,itemdos text)")
    conn.commit()
    conn.close()
    print("Connection created successfully...")

def test_insert(name,prize,quantity,dos):
    conn=sqlite3.connect("lang_connect.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO lang_connect VALUES (NULL,?,?,?,?)",(name,prize,quantity,dos))
    conn.commit()
    conn.close()
    #view()
    print('december_insert keyword is working so please move on...')

def test_exhibit():
    conn=sqlite3.connect("lang_connect.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM lang_connect")
    rows=cur.fetchall()
    conn.close()
    print(rows)

def test_delete(id):
    conn=sqlite3.connect("lang_connect.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM lang_connect WHERE id=?",(id,))
    conn.commit()
    conn.close()
    print('deleted successfully...')

#test_connect()
#test_insert('cats',20,10,22122020)
test_exhibit()
#test_delete(2)


todays_date = datetime.now()


todays_date.isocalendar()[1]
print(todays_date)

print('Hour:', todays_date.hour)

#to get minutes from datetime
print('Minute:',todays_date.minute)

#stuff = [('Brenda','smitherton','brenda@smitherton.com'),
#       ('Joshua','Raintree','joshua@raintree.com')]

#database.add_many(stuff)
#database.email_lookup("dan@pas.com")


#Delete Record use rowid as string
#database.delete_one('6')

#database.show_all()

x = int('3')
y = int('2')
print (x - y)

#get current date
datetime_object = datetime.now()
shaft = datetime_object.day
print(datetime_object)
print('Type:- ',type(datetime_object))
if shaft == 11:
    print('day:', shaft)
else:
    print("this is done...")
'''
'''
my_string = '2021-12-11'

#create date object in given time format yyyy-mm-dd
my_date = datetime.strptime(my_string,"%Y-%m-%d")

print(my_date)
print('Type: ', type(my_date))
print('Day of Month:',my_date.day)

#to get name of day(in number) from date
print('Day of Week (number):', my_date.weekday())

#to get name of day from date
print('Day of week(name):',calendar.day_name[my_date.weekday()])

cut = ['emeka','daniel','jude','emeratus','elephant','chisom']
for c in cut:
    if c.startWithe:
        print(cut)  

'''