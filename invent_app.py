from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import tkinter
from datetime import date
from datetime import timedelta
#import fileinput
import sys
# from tkcalendar import Calendar
from datetime import datetime
import invent_code



class Inventory:

    def __init__(self,root):
        self.root = root
        self.root.title("Inventory System")
        self.root.geometry("10000x3000+0+0")
        self.root.configure(background ='white')

        MainFrame = Frame(self.root, bd = 20, width = 990, height = 280,bg = "indigo", relief = RIDGE)
        MainFrame.grid()
        #declaring minimum and maximum size
        root.maxsize(350,360)
        root.minsize(350,300)
        self.labelNewProd = Label(MainFrame, text = "Add a new product")
        self.labelNewProd.grid(row=0,column = 0)

        self.btnNewProd = Button(MainFrame, text= "Click to Add a new product")
        self.btnNewProd.bind("<Button>",lambda e: NewWindow(self.root))

        self.btnNewProd.grid(row = 0,column = 1,pady = 10)

        self.labelViewStock = Label(MainFrame, text = "View Stock")
        self.labelViewStock.grid(row=1,column = 0)

        self.btnViewStock = Button(MainFrame, text= "Click to View Stock")
        self.btnViewStock.bind("<Button>", lambda e: NewWindow(self.root))

        self.btnViewStock.grid(row = 1,column = 1,pady = 10)

        self.labelInputSales = Label(MainFrame, text = "Input Sales Record")
        self.labelInputSales.grid(row=2,column = 0)

        self.btnInputSales = Button(MainFrame, text= "Click to Input Sales Record")
        self.btnInputSales.bind("<Button>", lambda e: NewWindow(self.root))

        self.btnInputSales.grid(row = 2,column = 1,pady = 10)


        self.labelInputExpenses = Label(MainFrame, text = "Input Expenses Record")
        self.labelInputExpenses.grid(row=3,column = 0)

        self.btnInputExpenses = Button(MainFrame, text= "Click to Input Expenses Record")
        self.btnInputExpenses.bind("<Button>", lambda e: NewWindow(self.root))

        self.btnInputExpenses.grid(row = 3,column = 1,pady = 10)

        self.labelRetrieveSales = Label(MainFrame, text = "Retrieve Sales Record")
        self.labelRetrieveSales.grid(row=4,column = 0)

        self.btnRetrieveSales = Button(MainFrame, text= "Click to Retrieve Sales Record")
        self.btnRetrieveSales.bind("<Button>", lambda e: NewWindow(self.root))

        self.btnRetrieveSales.grid(row = 4,column = 1,pady = 10)

        self.labelRetrieveExpenses = Label(MainFrame, text = "Retrieve Expenses Record")
        self.labelRetrieveExpenses.grid(row=5,column = 0)

        self.btnRetrieveExpenses = Button(MainFrame, text= "Click to Retrieve Expenses Record")
        self.btnRetrieveExpenses.bind("<Button>", lambda e: NewWindow(self.root))

        self.btnRetrieveExpenses.grid(row = 5,column = 1,pady = 10)

        self.labelDeleteRecord = Label(MainFrame, text = "Delete record")
        self.labelDeleteRecord.grid(row= 6,column= 0)

        self.btnDeleteRecord = Button(MainFrame, text = "click to delete record")
        self.btnDeleteRecord.bind("<Button>")

        self.btnDeleteRecord.grid(row = 6, column =1)


class NewWindow(Toplevel):

    def __init__(self,master =None):


        super().__init__(master=master)
        self.title("New Window")
        #self.root = root
        
        self.geometry("1000x300+0+0")
        self.configure(background ='indigo')
        #master.maxsize(300,200)
        #root.minsize(200,100)
        #================Frames=======================

        MainFrame = Frame(self, bd = 10, width =700, height =280, bg="white", relief = RIDGE)
        MainFrame.grid()
        

        LeftFrame = Frame(MainFrame, bd =5, width = 450, height = 280, padx=10, bg="white", relief =RIDGE)
        LeftFrame.pack(side = LEFT)

        
        RightFrame = Frame(MainFrame, bd =5, width = 500, height = 280, padx=10, bg="white", relief =RIDGE)
        RightFrame.pack(side = RIGHT)


        Description = StringVar()
        UnitPrice = float()
        Qty  = int()
        search_query = StringVar()
        salesvar = StringVar()
        descriptioncombovar = StringVar()
        salesqty = StringVar()
        ''' 
        product_list = []
        combo_dict = {}
        sales_list = []
        '''
        

        def std_format_func():
            std_d = Description.get() + (' '*(20 - len(Description.get())))
            std_p = UnitPrice.get() + (' '*(20 - len(UnitPrice.get())))
            std_q = Qty.get() + (' '*(20 - len(Qty.get())))

            product_list.append(std_d)
            product_list.append(std_p)
            product_list.append(std_q)

            return product_list
        '''
        def writer_func():
            with open('txt_file.txt','a') as file:
                file.write('\n')

                x = std_format_func()
                for item in x:
                    file.write(item)
                

            self.txtReceipt.insert(END,'File write operation successful')

        def reader_func(event):
            with open('txt_file.txt','r') as file:
                for line in file:
                    #print(line.strip().split())
                    
                    
                    for item in line.strip().split():
                        print(item,end=' ')

                        #print('\n')
                        self.txtReceipt.insert(END,item)

                    self.txtReceipt.insert(END,'\n')

        def search_func(event):
            with open('txt_file.txt','r') as file:
                for line in file:
                    if search_query.get() in line:
                        for item in line.strip().split():
                            self.txtReceipt.insert(END,item +'\t' )

        def update_combobox():
            with open('txt_file.txt','r') as file:
                for line in file:
                    if line[:19].strip()  in combo_dict.keys():
                        print('no new item to add')
                    else:
                        combo_dict[line[:19].strip()] = [line[20:39].strip(),line[40:59].strip()]
                    
                print(combo_dict)
                #for key in combo_dict.keys():
                    
                    #self.cboDescription['values'] = tuple(list(self.cboDescription['values']) + [str(key)])
                self.cboDescription['values'] = [key for key in combo_dict.keys()]
             

        def sales_writer():
            sales_list.append(standard(descriptioncombovar.get()))
            sales_list.append(standard(salesvar.get()))
            sales_list.append(standard(salesqty.get()))

            sales_list.append(str(datetime.now()))

            with open('salestxt_file.txt','a') as file:
                file.write('\n')

         
                for item in sales_list:
                    file.write(item)
                

            self.txtReceipt.insert(END,'File write operation successful')

        def sales_reader():
            pass
                
                
            
            

        def callfunc(event):
            salesvar.set(combo_dict[descriptioncombovar.get()][0])
            Spinbox(LeftFrame,from_ = 1, to =int(combo_dict[descriptioncombovar.get()][1]), font = ('arial',16,'bold'),textvariable = salesqty,fg = 'black', width = 14).grid(row = 5,column =2)



        def standard(word):
            word = word+(' '*(20-len(word)))



            return word

        def UpdateInventoryQty():

            #get the qty from the dictionary
            var = combo_dict[descriptioncombovar.get()][1]

            #subtract chosen qty from the total available qty
            newvar = str(int(var) - int(salesqty.get()))

            #update dictionary value
            combo_dict[descriptioncombovar.get()][1] = str(newvar)

            #populate the list with description,price and qty
            updated_list = [value for value in combo_dict[descriptioncombovar.get()]]
            updated_list.insert(0,descriptioncombovar.get())
            print(updated_list)
            

            for line in fileinput.input('txt_file.txt',inplace = 1):
                if line.strip().split()[:1] == updated_list[:1]:
                    #print('sighted')
                    line = line.replace(standard(var),standard(newvar))
                    sys.stdout.write(line)
                else:
                    sys.stdout.write(line)

                
            sales_writer()
            print('done')
            '''
        '''
        def grad_date():
            self.date.config(text = "Selected Date is: " + self.cal1.get_date())
            self.date2.config(text = "Second Date is: " + self.cal2.get_date())

        def date_timeconverter(stringg):
            date_time_obj = datetime.strptime(stringg,'%m/%d/%y')
            return date_time_obj

        def customfunc():
            x = date_timeconverter(self.cal1.get_date())
            y =date_timeconverter(self.cal2.get_date())
            reference_timestamp1 = x.timestamp() 
            reference_timestamp2 = y.timestamp()
            if reference_timestamp1 > reference_timestamp2:
                self.txtReceipt.insert(END,'The to date is less than the from date,Adjust the date and click the button again\n')
                return
            with open('salestxt_file.txt','r') as file:
                for line in file:
                    z =datetime.strptime(line.strip()[62:78],'%y-%m-%d %H:%M:%S')
                    if (z.timestamp()>= x.timestamp())and(z.timestamp()<= y.timestamp()):
                        self.txtReceipt.insert(END,line)
                        
                        '''
            
            
                           
        def callback(P):
            if str.isdigit(P) or P == "":
                return True
            else:
                return False

        def summary(event):
            self.txtReceipt.insert(END,'Description:\t\t\t\t' + Description.get()+ '\n' +'Price:\t\t\t\t'  + Price.get() + '\n' +'Qty:\t\t\t\t' + Qty.get() + '\n')
         

        #================LeftFrame=======================

        self.lblDescription =Label(LeftFrame, font =('arial',18, 'bold'), text = "product name:",padx =2,pady=2,bg="powder blue")
        self.lblDescription.grid(row =0,column=0, sticky = W)

        vcmd = (self.register(callback)) 
        self.txtDescription = Entry(LeftFrame,textvariable = Description)
        self.txtDescription.grid(row =0, column =1,sticky = W)

        self.lblUnitPrice =Label(LeftFrame, font =('arial',18, 'bold'), text = "Price:",padx =2,pady=2,bg="powder blue")
        self.lblUnitPrice.grid(row =1,column=0, sticky = W)

        
        self.txtUnitPrice = Entry(LeftFrame,textvariable = UnitPrice, validate = 'all',validatecommand = (vcmd, '%P'))
        self.txtUnitPrice.grid(row =1, column =1,sticky = W)

        self.lblQty =Label(LeftFrame, font =('arial',18, 'bold'), text = "Quantity:",padx =2,pady=2,bg="powder blue")
        self.lblQty.grid(row =2,column=0, sticky = W)

        self.txtQty = Entry(LeftFrame,textvariable =Qty, validate = 'all',validatecommand = (vcmd, '%P'))
        self.txtQty.grid(row =2, column =1,sticky = W)

        self.btnOk = Button(LeftFrame, text= "Click to Show Summary of Stocks added")
        self.btnOk.bind("<Button>", summary)

        self.btnOk.grid(row = 3,column = 0,pady = 10)

        self.btnAdd = Button(LeftFrame,command = invent_code.add, text= "Click to add to Inventory Record")
        self.btnAdd.bind("<Button>", summary)

        self.btnAdd.grid(row = 3,column = 1,pady = 10)

        self.btnOk = Button(LeftFrame, text= "Click to show current Stock")
        self.btnOk.bind("<Button>", summary)

        self.btnOk.grid(row = 3,column = 2,pady = 10)

        self.txtSearch = Entry(LeftFrame,textvariable = search_query)
        self.txtSearch.grid(row =4, column =0,sticky = W)


        self.btnSearch = Button(LeftFrame, text= "Click to search through current Stock",command = invent_code.search)
        self.btnSearch.bind("<Button>", invent_code.search)

        self.btnSearch.grid(row = 4,column = 1,pady = 10)


        self.cboDescription = ttk.Combobox(LeftFrame,font =('arial',18, 'bold'),textvariable = descriptioncombovar, state ='readonly'
                                        ,postcommand = update_combobox,width =19)
        self.cboDescription.bind("<<ComboboxSelected>>", callfunc)
        #self.cboProdType['value'] = ('','Lawnmower', 'Pickup Van', 'Cement Mixer', 'Elec. Generator')
        #self.cboDescription.current(0)
        self.cboDescription.grid(row =5,column=0)

        self.salesPricetext = Entry(LeftFrame,font =('arial',16, 'bold'),textvariable = salesvar ,
                                        fg = 'black' ,width =14).grid(row =5,column = 1)
        self.btnClose = Button(LeftFrame,text = "close",command = root.destroy)
        self.btnClose.bind("<Button>", summary)
        self.btnSearch.grid(row = 6,column = 0,pady = 10)


        '''
        
        self.updateQtybtn = Button(LeftFrame,command = UpdateInventoryQty, text= "Click to update current Stock").grid(row =6,column = 0)

        self.cal1 = Calendar(LeftFrame, selectmode = 'day', year = 2020, month = 5, day = 22)


        self.cal1.grid(row = 7,column = 0)


        self.cal2 = Calendar(LeftFrame, selectmode = 'day', year = 2020, month = 5, day = 22)


        self.cal2.grid(row =7,column = 1)
        Button(LeftFrame, text = "Get Date", command = customfunc).grid(row = 7,column =2)

        self.date   = Label(LeftFrame, text = "")
        self.date.grid(row = 8,column =0)

        self.date2   = Label(LeftFrame, text = "")
        self.date2.grid(row = 8,column = 1)
            '''
    



        

        #self.salesQtySpin = Spinbox(LeftFrame,font = ('arial',16,'bold'),textvariable = salesqty,fg = 'black', width = 14).grid(row = 5,column =2)
        #===============RightFrame=======================

        self.txtReceipt = Text(RightFrame, font=('arial',9,'bold'))
        self.txtReceipt.pack()
        



        

        

        
        # so i am to create another window for bought items so that when items bought are entered it will automatically decrement it from the remaining.
        #change the prize and quantity of an item.
        # how to create an interactive messagebox in tkinter

if __name__ == "__main__":
    root = Tk()
    application = Inventory(root)

    
    root.mainloop()
