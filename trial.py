# importing tkinter
from tkinter import*

#initializing root
root = Tk()
class flesc():
	#setting geometry
	#root.geometry("400x300")
	root.maxsize(5000,5000)
	root.minsize(1000,800)
	#defining function to print username and password on call
	def showInfo():
		print("User Name is:",user_name.get())
		print("password is:", password.get())
	def real():
		get.user_name=="welcome"
		get.password=="howfar"
		if user_name == "welcome" & password == 'howfar':
			Button1= Button(text = 'print',command =real).pack(pady = 10)
	#defining function to clear entry widgets using .set() method
	def clear():
	
		user_name.set("")
		password.set("")
	user_name = StringVar() #user name variable
	password = StringVar() # password variable


	#creating an entry widget to take user password
	user_name_Entry = Entry(textvariable = user_name).pack(pady = 10)
	#creating an entry
	passEntry = Entry(textvariable = password, show = '*').pack(pady = 10)

	Button1= Button(text = 'Show Info',command =showInfo).pack(pady = 10)
	Button2 =Button( text = 'clear info',command = clear).pack(pady = 10)
	Button3 =Button( text = 'close',command = root.destroy ).pack(pady = 10)

#photo = PhotoImage()
#label = Label(root,image = photo)
#label.pack()
leg = flesc()
root.mainloop()