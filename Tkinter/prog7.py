from Tkinter import *

root = Tk()

def leftClick(event):
	label_1 = Label(root, text="Left Click")
	label_1.pack()

def rightClick(event):
	label_2 = Label(root, text="Right Click")
	label_2.pack()

frame = Frame(root, width=300, height=250)
#if the height and width is not specifies here, then the window will not be rendered on the screen as there are no other widgets to display
frame.bind("<Button-1>", leftClick)
#catches the event left click on the frame
frame.bind("<Button-3>", rightClick)
#catches the event right click on the frame
frame.pack()

root.mainloop()