from Tkinter import *

root = Tk()

topFrame = Frame(root, width= 300, height=250)
topFrame.pack()
#Argument 1- window where you want to place the frame
#Argument 2- specifies width of the frame in pixels
#Argument 3- specifies height of the frame in pixels

bottomFrame = Frame(root)
bottomFrame.pack(side= BOTTOM)
#bottom frame goes on the bottom on the page and top frame goes on top automatically

button1 = Button(topFrame, text="First Button on Top Frame", fg="brown", bg="white")
button2 = Button(topFrame, text="Second Button on Top Frame", fg="blue")
button3 = Button(topFrame, text="Third Button on Top Frame", fg="red")
button4 = Button(bottomFrame, text="First Button on Bottom Frame", fg="purple")
button5 = Button(bottomFrame, text="Second Button on Bottom Frame", fg="green")
#Argument 1- where you want to place the button
#Argument 2- text that you want the button to display
#Argument 3- foreground color: set the color of the text displayed(optional)
#Argument 4- set the background color(optional)
#Argument 5- (command= "") action that the button should take when clicked
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack()
button5.pack()
#the side parameter specifies the position of the button. The defalut is set to bottom i.e. they are stacked one on top of another
#when we say side as left, the button is packed to the leftmost side of the frame and this happens similarly for all the subsequent buttons that are packed onto the frame

root.mainloop()