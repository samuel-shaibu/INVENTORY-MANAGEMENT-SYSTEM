from tkinter import*
#from PIL import ImageTk, Image
from tkinter import ttk
from functools import partial
import collector
import datetime as dt
from datetime import datetime
import customer_data
import laden
from datetime import date
import december
import november
import october
import september
import august
import july
import june
import may
import april
import march
import febuary
import january
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import winsound
import expenses
class Inventory:
    def __init__(self,root):
        self.root = root
        self.root.title("NASCOMSOFT INVENTORY MANAGEMENT SYSTEM")
        self.root.geometry("10000x3000+0+0")
        self.root.configure(background = 'white')
        
        messagebox.showinfo('ATTENTION!!!','PLEASE MAKE SURE YOUR PC DATE AND TIME ARE SET CORRECTLY AS THE SOFTWARE WILL MAKE USE OF THEM')
        #create an instance of datetime module
        date = dt.datetime.now()
        #format the date
        format_date = f"{date:%a, %b %d %y, %H:%M:%S}"
        print(format_date)
        def view_table():
            self.root.list1.delete(0,END)
            for info in collector.display():
                self.root.list1.insert(END,info)

        def hit_selected_row(event):
            global selected_tuple     
            try:       
                index = self.root.list1.curselection()[0]
                selected_tuple = self.root.list1.get(index)
            except IndexError:
                print('error handle successful...')
            self.root.e1.delete(0,END)
            self.root.e1.insert(END,selected_tuple[1])
            self.root.e2.delete(0,END)
            self.root.e2.insert(END,selected_tuple[2])
            self.root.e3.delete(0,END)
            self.root.e3.insert(END,selected_tuple[3])
        def purchase_add():
                hint =date
                flaws = hint.day
                catcher = hint.month
                if catcher == 12 :
                    december.december_insert(search_info.get(), price_purchase.get(),quantity_purchase .get(),DOS.get())
                    winsound.Beep(800,460)
                    print('The month of december ')            
                elif catcher == 11: 
                    november.november_insert(search_info.get(), price_purchase.get(),quantity_purchase .get(),DOS.get())
                    print('The month of november' )
                    winsound.Beep(800,460)
                    print(catcher)
                elif catcher == 10:
                    october.october_insert(search_info.get(), price_purchase.get(),quantity_purchase .get(),DOS.get())
                    winsound.Beep(800,460)
                    print('The month of october ')
                    print(catcher)   
                elif catcher == 9 :
                    september.september_insert(search_info.get(), price_purchase.get(),quantity_purchase .get(),DOS.get())
                    winsound.Beep(800,460)
                    print('The month of september')
                    print(catcher)
                elif catcher == 8 :
                    august.august_insert(search_info.get(), price_purchase.get(),quantity_purchase .get(),DOS.get())
                    winsound.Beep(800,460)
                    print('The month of august ')
                    print(catcher)
                elif catcher == 7 :
                    july.july_insert(search_info.get(), price_purchase.get(),quantity_purchase .get(),DOS.get())
                    winsound.Beep(800,460)
                    print('The month of july ')
                    print(catcher) 
                elif catcher == 6 :
                    june.june_insert(search_info.get(), price_purchase.get(),quantity_purchase .get(),DOS.get())
                    winsound.Beep(800,460)
                    print('The month of june ')
                    print(catcher) 
                elif catcher == 5 :
                    may.may_insert(search_info.get(), price_purchase.get(),quantity_purchase .get(),DOS.get())
                    winsound.Beep(800,460)
                    print('The month of may ')
                    print(catcher)
                elif catcher == 4 :
                    april.april_insert(search_info.get(), price_purchase.get(),quantity_purchase .get(),DOS.get())
                    winsound.Beep(800,460)
                    print('The month of april ')
                    print(catcher)
                elif catcher == 3 :
                    march.march_insert(search_info.get(), price_purchase.get(),quantity_purchase .get(),DOS.get())
                    winsound.Beep(800,460)
                    print('The month of march')
                    print(catcher)
                elif catcher == 2 :
                    febuary.febuary_insert(search_info.get(), price_purchase.get(),quantity_purchase .get(),DOS.get())
                    winsound.Beep(800,460)
                    print('The month of febuary')
                    print(catcher)
                elif catcher == 1:
                    january.january_insert(search_info.get(), price_purchase.get(),quantity_purchase .get(),DOS.get())
                    winsound.Beep(800,460)
                    print('The month of january ')
                    print(catcher)
                else:
                    print('we are still in december')
                    #how can i compile records over a certain period of time?
                    #i think i will use month, if it is in so..so and so.. month it should insert into the database.        
           
        def clear():
            self.root.list1.delete(0,END)

        def quit():
            if messagebox.askokcancel("Quit", 'Are you sure you want quit?'):
                root.destroy()

        #__________________________MainFrame_______________________
        Mainframe = Frame(self.root,bg = '#0aa0af',bd = 20,width = 1000,height = 500, relief = RIDGE)
        Mainframe.grid()
        #root.maxsize(5000,1000)

        #self.root.status = Label(self.root,text = "TECHNOLOGY FOR ALL",bd = 2,relief = SUNKEN,anchor = W)
        #self.root.status.grid(row =10 , column = 0)

        self.root.btn1 = Button(Mainframe, bg = 'white', width = 20,height = 1, text = 'ADD ITEM',command = Login,bd = 10, padx = 2)
        self.root.btn1.grid(row = 1,column = 0)
        
        self.root.btn1 = Button(Mainframe, bg = 'white', width = 20, height  = 1, text = 'UPDATE', command = Login, bd = 10, padx = 2)
        self.root.btn1.grid(row = 1,column = 2)
        
        self.root.btn1 = Button(Mainframe, bg = 'white', width = 20,height = 1, text = 'PURCHASE ITEM',bd = 10, padx = 2,command = purchase_add)
        self.root.btn1.grid(row = 0,column = 0)
        search_info = StringVar()
        
        self.root.e1 = Entry(Mainframe, bg = 'white', width = 20, textvariable = search_info)
        self.root.e1.grid(row = 0, column = 1)

        self.root.label = Label(Mainframe,bg = "white", width = 3, height = 1,fg = 'black',bd = 2,padx = 2,text = 'PRICE',)
        self.root.label.grid(row =0, column = 2)
        price_purchase = StringVar()

        self.root.e2 = Entry(Mainframe, bg = 'white', width = 10, textvariable = price_purchase)
        self.root.e2.grid(row = 0, column = 3)

        self.root.label = Label(Mainframe,bg = "white", width = 7, height = 1,fg = 'black',bd = 2,padx = 2,text = 'QUANTITY')
        self.root.label.grid(row =0, column = 4)
        quantity_purchase = StringVar()

        self.root.e3 = Entry(Mainframe, bg = 'white', width = 20, textvariable = quantity_purchase)
        self.root.e3.grid(row = 0, column = 6)
        
        
        self.root.label = Label(Mainframe,bg = "white", width = 7, height = 1,fg = 'indigo',bd = 2,padx = 2,text = 'DATE&TIME')
        self.root.label.grid(row =0, column = 7)
        DOS = StringVar()
        self.root.e4 = Entry(Mainframe,bg = 'white', width = 22,textvariable = DOS)
        self.root.e4.grid(row = 0,column = 8)
        self.root.e4.insert(END, format_date)

        self.root.btn1 = Button(Mainframe, bg = 'white', width = 5, command = clear,height = 1, text = 'Clear',bd = 10, padx = 2)
        self.root.btn1.grid(row = 3,column = 3)
        
        self.root.btn1 = Button(Mainframe, bg = 'white', width = 20,height = 1,command =Login, text = 'DELETE RECORD',bd = 10, padx = 2)
        self.root.btn1.grid(row = 2,column = 0)
        
        self.root.btn1 = Button(Mainframe, bg = 'white', width = 20,height = 1, text = 'VIEW ITEM',bd = 10, padx = 2, command = view_table)
        self.root.btn1.grid(row = 2,column = 2)
        
        self.root.btn1 = Button(Mainframe, bg = 'white', width = 20,command = quit,height = 1,text = 'CLOSE',bd = 10, padx = 2)
        self.root.btn1.grid(row = 3,column = 0)
        
        
        self.root.btn1 = Button(Mainframe, bg = 'white', width = 20,height = 1, text = 'SALES RECORD',bd = 10, padx = 2,command = Login)
        self.root.btn1.grid(row = 3,column = 2)
        #self.root.btn1.bind("<Button>",lambda e: Login(master))

        #how can i give my listbox subheadings
        self.root.list1 = Listbox(Mainframe, height =  10, width = 60,bd = 3)
        self.root.list1.grid(row = 5,column =0,rowspan = 6,columnspan = 6)
        self.root.list1.bind('<<ListboxSelect>>',hit_selected_row)

        sb1 = Scrollbar(Mainframe)
        sb1.grid(row = 5, column = 4,rowspan = 6)

        self.root.list1.configure(yscrollcommand = sb1.set)
        sb1.configure(command = self.root.list1.yview)
        
        img =ImageTk.PhotoImage(Image.open(os.path.join("C:\\sqlite","colour_trace_Nas.jpg")))
        labek = Label(image=img,relief = SUNKEN)
        labek.photo = img
        labek.config(bg = 'gray51',fg = 'white')
        labek.grid(row = 3, column = 9)

#how to assign multiple functions inside the toplevel window
#adding multiple window to a window in tkinter
        
        #creating another window
class Login(Toplevel):

    def __init__(self,master =None):


        super().__init__(master=master)
        self.title("LOGIN WINDOW")
        #self.root = root
        
        self.geometry("1000x300+0+0")
        self.configure(background ='#0aa0af')
        self.maxsize(900,140)
        self.minsize(700,40)
        #================Frames=======================

        MainFrame = Frame(self, bd = 10, width =1000, height =280, bg="white", relief = RIDGE)
        MainFrame.grid()
        '''
        saleslabel = Label(MainFrame, text = 'RECORD')
        saleslabel.grid(row = 2,column = 0)        
        '''

        #defining login function
        def login():
            #getting form data
            uname = username.get()
            pwd = password.get()
            #applying empty validation
            if uname == '' or pwd == '':
                message.set("please login to continue!!!")
            else:
                #pass:luck@11#
                if uname =="boy" and pwd == "11":
                    message.set("Login successful")
                    uname= username.set("")
                    pwd= password.set("")
                    # creating a new window
                    new_window = Toplevel()
                    new_window.title("RECORDS")
                    new_window.geometry("1000x3000+0+0")
                    new_window.configure(background = '#0aa0af')
                    new_window.maxsize(1350,1300)
                    new_window.minsize(1350,1000)

                    def customer_included():
                        customer_data.insert( customer_name.get(),phone_number.get(),sold_date.get())
                        list2.delete(0,END)
                        list2.insert(END,customer_name.get(),phone_number.get(),sold_date.get())
                    
                    def view_command():
                        list2.delete(0,END)
                        for row in customer_data.view():
                            list2.insert(END,row)

                    Label(new_window,text = "customer informations",width = 30, height = 1,bg = '#0aa0af',fg = 'white').grid(row = 0,column = 0)
                    MainFrame = Frame(new_window, bd = 10, width =1000, height =500, bg="white", relief = RIDGE)
                    MainFrame.grid()
                    
                    Label(MainFrame,text = "customer name").grid(row = 1,column = 0)
                    customer_name = StringVar()
                    
                    Entry(MainFrame,width = 45,textvariable = customer_name).grid(row = 1,column =1)
                    Label(MainFrame, text = "phone number").grid(row = 1,column = 2)
                    phone_number = StringVar()
                    
                    Entry(MainFrame, textvariable = phone_number, width = 40).grid(row = 1,column =3)
                    Label(MainFrame,text = "sold date").grid(row =1,column = 4)
                    sold_date = StringVar()
                    
                    Entry(MainFrame,textvariable = sold_date,width = 35).grid(row = 1,column = 5)
                    Button(MainFrame,text = "SAVE",bg = 'green',width = 10,height = 1,fg = 'white',command=customer_included).grid(row = 2, column = 0)
                    
                    #adding a add function
                    def get_selected_row(event):
                        global selected_tuple
                        index = list2.curselection()[0]
                        selected_tuple = list2.get(index)
                        e1.delete(0,END)
                        e1.insert(END,selected_tuple[1])
                        e2.delete(0,END)
                        e2.insert(END,selected_tuple[2])
                        e3.delete(0,END)
                        e3.insert(END,selected_tuple[3])

                    def add_command():
                        collector.input(ITEM_NAME.get(),PRICE.get(),QUANTITY.get())
                        list2.delete(0,END)
                        list2.insert(END,ITEM_NAME.get(),PRICE.get(),QUANTITY.get())

                    def view_decSales():
                        list2.delete(0,END)
                        for row in december.december_exhibit():
                            list2.insert(END,row)

                    def view_novSales():
                        list2.delete(0,END)
                        for row in november.november_exhibit():
                            list2.insert(END,row)

                    def view_octSales():
                        list2.delete(0,END)
                        for row in october.october_exhibit():
                            list2.insert(END,row)

                    def view_septSales():
                        list2.delete(0,END)
                        for row in september.september_exhibit():
                            list2.insert(END,row)               
                        
                    def view_augSales():
                        list2.delete(0,END)
                        for row in august.august_exhibit():
                            list2.insert(END,row)               
                    
                    def view_julSales():
                        list2.delete(0,END)
                        for row in july.july_exhibit():
                            list2.insert(END,row)               
                    
                    def view_junSales():
                        list2.delete(0,END)
                        for row in june.june_exhibit():
                            list2.insert(END,row)               
                    
                    def view_maySales():
                        list2.delete(0,END)
                        for row in may.may_exhibit():
                            list2.insert(END,row)               
                    
                    def view_aprSales():
                        list2.delete(0,END)
                        for row in april.april_exhibit():
                            list2.insert(END,row)               
                    
                    def view_marSales():
                        list2.delete(0,END)
                        for row in march.march_exhibit():
                            list2.insert(END,row)               
                    
                    def view_febSales():
                        list2.delete(0,END)
                        for row in febuary.febuary_exhibit():
                            list2.insert(END,row)               
                    
                    def view_janSales():
                        list2.delete(0,END)
                        for row in january.january_exhibit():
                            list2.insert(END,row)               
                    

                    def search_command1():
                        list2.delete(0,END)
                        for row in collector.find(delete.get()):
                            list2.insert(END,row)
                    
                    def delete_command():
                        collector.remove(selected_tuple[0])
                    
                    def delete_command2():    
                        customer_data.delf(selected_tuple[0])
                        #laden.dry(selected_tuple[0])
                    
                    def  delete_command1():
                        d1 = datetime.now()
                        relax = d1
                        ok = relax.month
                        if ok == 12:
                            december.dec_delete(selected_tuple[0])
                        elif ok == 11:
                            november.nov_delete(selected_tuple[0])
                        elif ok == 10:
                            october.oct_delete(selected_tuple[0])
                        elif ok == 9:
                            september.sept_delete(selected_tuple[0])
                        elif ok == 8:
                            august.aug_delete(selected_tuple[0])
                        elif ok == 7:
                            july.jul_delete(selected_tuple[0])
                        elif ok == 6:
                            june.jun_delete(selected_tuple[0])
                        elif ok == 5:
                            may.may_delete(selected_tuple[0])
                        elif ok == 4:
                            april.apr_delete(selected_tuple[0])
                        elif ok == 3:
                            march.mar_delete(selected_tuple[0])
                        elif ok == 2:
                            febuary.feb_delete(selected_tuple[0])
                        elif ok == 1:
                            january.jan_delete(selected_tuple[0])

                    def update_command():
                        collector.improve(selected_tuple[0],ITEM_NAME1.get(),PRICE1.get(),QUANTITY1.get())   
                        #print(selected_tuple[0],ITEM_NAME1.get(),PRICE1.get(),QUANTITY1.get())

                    NextFrame = Frame(new_window,bd = 10, width =1000, height =500, bg="white", relief = RIDGE)
                    NextFrame.grid()
                    
                    Label(NextFrame,text = "ADD ITEMS",width = 10, height = 1).grid(row = 3, column = 2)
                    Label(NextFrame,text = "ITEM NAME",width = 10).grid(row = 4,column = 0)
                    ITEM_NAME = StringVar()
                    
                    Entry(NextFrame,width = 40,textvariable = ITEM_NAME).grid(row = 4, column = 1)
                    Label(NextFrame,text = "PRICE",width = 10).grid(row = 4,column = 2)
                    PRICE = StringVar()
                    
                    Entry(NextFrame,width = 40,textvariable = PRICE).grid(row = 4, column = 3)
                    Label(NextFrame,text = "QUANTITY",width = 10).grid(row = 4,column = 4)
                    QUANTITY = StringVar()
                    
                    Entry(NextFrame,width = 40,textvariable = QUANTITY).grid(row = 4, column = 5)
                    Button(NextFrame,text = "ADD",bg = 'green',width = 10,height = 1,fg = 'white',command = add_command).grid(row = 5, column = 0)

                    NextFrame1 = Frame(new_window,bd = 10,width =1000,height = 500, bg = "white",relief = RIDGE)
                    NextFrame1.grid()
                    Label(NextFrame1,text = "UPDATE ITEMS",width = 12, height = 1).grid(row = 5, column = 2)
                    Label(NextFrame1,text = "ITEM NAME",width = 10).grid(row = 6,column = 0)
                    ITEM_NAME1 = StringVar()
                    
                    e1=Entry(NextFrame1,width = 40,textvariable = ITEM_NAME1)
                    e1.grid(row = 6, column = 1)
                    Label(NextFrame1,text = "PRICE",width = 10).grid(row = 6,column = 2)
                    PRICE1 = StringVar()
                    
                    e2=Entry(NextFrame1,width = 40,textvariable = PRICE1)
                    e2.grid(row = 6, column = 3)
                    Label(NextFrame1,text = "QUANTITY",width = 10).grid(row = 6,column = 4)
                    QUANTITY1 = StringVar()
                    
                    e3=Entry(NextFrame1,width = 40,textvariable = QUANTITY1)
                    e3.grid(row = 6, column = 5)
                    Button(NextFrame1,text = "UPDATE",command = update_command,bg = 'green',width = 10,height = 1,fg = 'white').grid(row = 7, column = 0)
                    
                    NextFrame2 = Frame(new_window,bd = 10,width =1000,height = 500, bg = "white",relief = RIDGE)
                    NextFrame2.grid()
                    
                    Label(NextFrame2,text = "DELETE ITEMS",width = 12, height = 1).grid(row = 8, column = 0)
                    Label(NextFrame2,text = "ITEM NAME",width = 12, height = 1).grid(row = 9, column = 0)
                    
                    delete = StringVar()
                    Entry(NextFrame2, textvariable = delete).grid(row = 9,column = 1)
                    
                    Button(NextFrame2, text = "DELETE ITEMS",command = delete_command, bg = 'red',fg = 'white',width = 10, height = 2).grid(row = 10,column = 0)
                    Button(NextFrame2, text = "SEARCH",command = search_command1,bg = 'gold',fg = 'white',width = 10, height = 2).grid(row = 10,column = 1)
                    
                    Button(NextFrame2, text = "DELETE RECORD",command = delete_command1, bg = 'pink',fg = 'black',width = 14, height = 2).grid(row = 10,column = 2)
                    Button(NextFrame2, text = "DELETE CUSTOMER \nINFO",command = delete_command2, bg = 'white',fg = 'red',width = 16,height = 3).grid(row = 10,column = 3)
                    
                    def include_expenses():
                        expenses.add_expenses(expensesname.get(),exquantity.get(),expensesprice.get(),dateVar.get())
                        list2.delete(0,END)
                        list2.insert(END,expensesname.get(),exquantity.get(),expensesprice.get(),dateVar.get())

                    def display_expenses():
                        list2.delete(0,END)
                        for rows in expenses.view_expenses():
                            list2.insert(END,rows)

                    supframe = Frame(new_window, bd = 5, width = 20, height = 50, bg = 'white', relief = SUNKEN)
                    supframe.grid(row = 5, column = 1)
                    
                    ExpensesFrame = Frame(supframe, bd = 2, width = 20,height = 10, bg = 'white', relief = SUNKEN)
                    ExpensesFrame.grid()
                    
                    labelexpenses = Label(supframe,text = "DAILY EXPENSES",padx = 2, font = "arial_black")
                    labelexpenses.grid(row= 2,column =0)
                    
                    expensename = Label(ExpensesFrame, text = "EXPENSES",width = 13,height = 1)
                    expensename.grid(row = 3, column =0)
                    expensesname = StringVar() 

                    expensesentry = Entry(ExpensesFrame, textvariable = ' expensesname')
                    expensesentry.grid(row = 3,column = 1)

                    expensesquantity = Label(ExpensesFrame, text = "QUANTITY",width =8,height = 1)
                    expensesquantity.grid(row = 4,column = 0)
                    exquantity = StringVar()

                    expensesquantity = Entry(ExpensesFrame,textvariable = ' exquantity')
                    expensesquantity.grid(row = 4, column = 1)

                    expenseprice = Label(ExpensesFrame, text = "PRICE",width = 5, height = 1)
                    expenseprice.grid(row = 5, column = 0)
                    expensesprice = StringVar()

                    expenseprice = Entry(ExpensesFrame, textvariable = 'expensesprice')
                    expenseprice.grid(row = 5, column = 1)

                    dateLabel = Label(ExpensesFrame,text = 'date')
                    dateLabel.grid(row= 6, column = 0)
                    dateVar = StringVar()

                    dateEn = Entry(ExpensesFrame, textvariable = 'dateVar')
                    dateEn.grid(row =6,column = 1)

                    exbutton = Button(ExpensesFrame, text = 'SAVE',  command = include_expenses, bg = 'green', fg = 'white')
                    exbutton.grid(row = 7, column = 0)
                    
                    
                    exbutview = Button(ExpensesFrame,command = display_expenses,text = "VIEW MONTHLY EXPENSES",bg = 'white')
                    exbutview.grid(row = 7,column = 1)

                    '''
                    Addpicture= Frame(NextFrame2, bd = 2, width = 10, height = 10,bg = "cyan",relief = SUNKEN)
                    Addpicture.grid(row = 10, column = 4)

                    deathwing = Image.open("C:\\sqlite","colour_trace_Nas.jpg")
                    image2 = deathwing.resize((10,10),Image.ANTIALIAS)
                    deathwing2 = ImageTk.PhotoImage(image2)
                    '''

                    NextFrame3 = Frame(new_window,bd = 10,width =1000,height = 500, bg = "white",relief = RIDGE)
                    NextFrame3.grid(row= 5,column=0)
                    #NextFrame3.maxsize(1000,100)
                    def open_software():
                        os.startfile("C:\\sqlite\\sqlitestudio-3.3.3\\SQLiteStudio\\sqlitestudio")
                    Label(NextFrame3,text = "SALES",width = 12, height = 1).grid(row = 0, column = 0)

                    Button(NextFrame3,bg = 'red',fg = 'white',bd = 4, text = "CLOSE",width = 13, command = new_window.destroy ,height = 2).grid(row = 1,column = 0)
                    Button(NextFrame3, text = "CUSTOMERS INFO",width = 15, height = 2,command = view_command).grid(row = 1,column = 2)
                    Button(NextFrame3,bg = 'blue',fg = 'white',bd = 4, text = "PRINT RECORD",width = 15,command= open_software, height = 2).grid(row = 1,column = 1)
                    #Button(NextFrame3,bg = 'gold',fg = 'red',bd = 4, text = "SEND REPORT",width = 13, height = 2).grid(row = 10,column = 4)
                    
                    Button(NextFrame3, text = "DEC SALES",width = 10, height = 1,command = view_decSales).grid(row = 2,column = 0)
                    Button(NextFrame3, text = "NOV SALES",width = 10, height = 1,command = view_novSales).grid(row = 3,column = 0)
                    Button(NextFrame3, text = "OCT SALES",width = 10, height = 1,command = view_octSales).grid(row = 4,column = 0)
                    
                    Button(NextFrame3, text = "SEPT SALES",width = 10, height = 1,command = view_septSales).grid(row = 5,column = 0)
                    Button(NextFrame3, text = "AUG SALES",width = 10, height = 1,command = view_augSales).grid(row = 6,column = 0)
                    Button(NextFrame3, text = "JULY SALES",width = 10, height = 1,command = view_julSales).grid(row = 7,column = 0)
                    
                    Button(NextFrame3, text = "JUNE SALES",width = 10, height = 1,command = view_junSales).grid(row = 2,column = 1)
                    Button(NextFrame3, text = "MAY SALES",width = 10, height =  1,command = view_maySales).grid(row = 3,column = 1)
                    Button(NextFrame3, text = "APRIL SALES",width = 10, height = 1,command = view_aprSales).grid(row = 4,column = 1)

                    Button(NextFrame3, text = "MARCH SALES",width = 10, height = 1,command = view_marSales).grid(row = 5,column = 1)
                    Button(NextFrame3, text = "FEB SALES",width = 10, height = 1,command = view_febSales).grid(row = 6,column = 1)
                    Button(NextFrame3, text = "JAN SALES",width = 10, height = 1,command = view_janSales).grid(row = 7,column = 1)

                    list2 = Listbox(NextFrame3, height =  10, width = 60,bd = 3)
                    list2.grid(row = 2,column =2,rowspan = 6,columnspan = 6)
                    list2.bind('<<ListboxSelect>>',get_selected_row)

                    sb2 = Scrollbar(NextFrame3)
                    sb2.grid(row = 2, column = 8,rowspan = 6)

                    list2.configure(yscrollcommand = sb2.set)
                    sb2.configure(command = list2.yview)




                else:
                    message.set("Wrong username or password!!!")
        global message;
        global username
        global password
        username = StringVar()        
        password = StringVar()
        message = StringVar() 
        # creating layout of login
        Label(MainFrame, width = "50", text = "please enter details below", bg = '#0aa0af', fg = 'white').grid(row = 0, column = 0)
        #username label
        Label(MainFrame, text = "Username * ").grid(row = 1,column = 0,)
        #username textbox
        let = Entry(MainFrame, textvariable =username)
        let.grid(row =1, column =1)
        let.focus()
        #password Label
        Label(MainFrame, text = "password * ").grid(row = 2,column = 0)
        #password textbox
        Entry(MainFrame,textvariable = password, show = '*').grid(row = 2,column = 1)
        #Label for displaying login status[success/failed]
        Label(MainFrame,text = "",textvariable = message).grid(row = 3,column = 0)
        #Login Button
        Button(MainFrame, text = "Login",width = 10,height = 1,fg = 'white',bg = '#0aa0af',command = login).grid(row = 3,column = 1)
        Button(MainFrame, text = "CLOSE",width = 10, height = 1,bg = 'red',fg = 'white',command = self.destroy).grid(row=4,column = 0)
    
        username.set("")
        password.set("")


       
root = Tk()
app = Inventory(root)
#shop = Login(root)
root.mainloop()