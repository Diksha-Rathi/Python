from Tkinter import *

root = Tk()

label_1 = Label(root, text= "Username")
label_2 = Label(root, text= "Password")
entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=0, sticky=E)
label_2.grid(row=1,sticky=E)
#sticky E implies right aligned

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1) 

c = Checkbutton(root, text="Keep me logged in")
#Argument 1- spedifies the window to place the checkbox
#Argument 2- specifies the text to display on the right of the checkbox
#for more- http://www.tutorialspoint.com/python/tk_checkbutton.htm
c.grid(columnspan=2)
#to make a widget span on multiple columns use the argument columnspan (default alignment is center aligned)

root.mainloop()