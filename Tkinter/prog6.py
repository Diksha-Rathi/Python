from Tkinter import *

root = Tk()

#Method1
def printName_M1():
	label1 = Label(root, text="My name is Diksha.")
	label1.pack()

button1 = Button(root, text="Print my name using command argument", command=printName_M1)
button1.pack()

#Method2
#the event here can be a scroll, mouse movement, button click on the keyboard etc.
def printName_M2(event):
	print("My name is Diksha")

button2 = Button(root, text="Print my name using event listener")
button2.bind("<Button-1>", printName_M2)
#Argument 1- specifies the event to listen to(button- 1 specifies left click of mouse button)
#Argument 2- specifies what to do when event in argument 1 occurs
button2.pack()

root.mainloop()