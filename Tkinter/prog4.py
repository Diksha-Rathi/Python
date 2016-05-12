from Tkinter import *

root = Tk()

label_1 = Label(root, text= "Username")
label_2 = Label(root, text= "Password")

#creates two input fields to accept the above entries
entry_1 = Entry(root)
entry_2 = Entry(root)
#this displays a one line input field on the screen to accept a value
#its only argument is the window where you wish to place the input field

#the following lines use the grid layout(this may be considered as an excel sheet)
#it has two arguments- row and column wherein the default value for only column is zero
#the default alignment is center aligned
label_1.grid(row=0)
label_2.grid(row=1)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1) 

root.mainloop()