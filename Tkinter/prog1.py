from Tkinter import *

root = Tk()
#creates a blank window

thelabel = Label(root, text= "Hello, World!")
#Argument 1- Specify the window where you need to place the text
#Argument 2- Text that you want to display on screen

thelabel.pack()
#fix it on the window

root.mainloop()
#this goes to an infinite loop enabling window to be displayed continuously until the user clicks the close button
