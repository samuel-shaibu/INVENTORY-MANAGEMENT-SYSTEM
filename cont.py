#import module
from tkinter import *
# create object
root = Tk()

#Adjust size
root.geometry("400x400")

#Add image file
bg = PhotoImage(file = "colour_trace_Nas.jpg")

#Create Canvas
canvas1 = Canvas(root,width = 400, height = 400)
canvas1.pack(fill = "both",expand = True)

#Display Imagedddddddd
canvas1.create_image(0,0, image = bg, anchor = "nw")
#Add text
canvas1.create_image(200,250, text = "welcome")

#create Buttons
button1 = Button(root,text = "Exit")
button2 = Button(root, text = "Start")
button3 = Button(root, text ="Reset")

#display Buttons
button1_canvas = canvas1.create_window(100,10,anchor = "nw", window = button1)
button2_canvas = canvas1.create_window(100,40, anchor = "nw", window = button2)
button3_canvas = canvas1.create_window(100, 70,anchor = "nw",window = button3)

#Execute Tkinter
root.mainloop()