from Tkinter import *

root = Tk()

one = Label(root, text= "Label 1", bg="Yellow", fg="Brown")
one.pack()

second = Label(root, text= "Label 2", bg="White", fg="Purple")
second.pack(fill=X)
#the command fill X makes the label responsive to the size of the window in the X- direction i.e. as the size of the window increases, the space occupied by label is also increased in the X- direction
#if the above argument is not added, then the space taken by label remains same irrespective of the window size

three = Label(root, text= "Label 3", bg="Black", fg="Pink")
three.pack(side= RIGHT,fill=Y)
#when fill is set to Y, the scaling takes place only in the Y- direction

#the default value for side is TOP. So, if side is not set to right or left, then you will not be able to notice any changes.
#you cannot set fill to both X and Y as the argument cannot be repeated in declaration
#the bg argument helps us to understand better what has been discussed above

#button1 = Button(root, text="abc")
#button1.pack(side=LEFT, fill=Y)
#works on all widgets

root.mainloop()