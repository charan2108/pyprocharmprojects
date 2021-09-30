# from tkinter import *
# root =Tk()
# root.mainloop()

# pack grid place methods
# pack method
# from tkinter import *
# root =Tk()
# myLabel =Label(root, text="Hello World!")

# myButton = Button(root, text = 'A', fg="red")
# myButton1 = Button(root, text = 'B', fg="blue")
# myButton2 = Button(root, text = 'C', fg="red")
# myButton3 = Button(root, text = 'D', fg="blue")
# myButton.pack(side=LEFT)
# myButton1.pack(side=RIGHT)
# myButton2.pack(side=TOP)
# myButton3.pack(side=BOTTOM)
# root.mainloop()

# grid method

from tkinter import *
root =Tk()
myLabel = Label(root, text="gridmethod")
name = Label(root, text="Name").grid(row=0, column=0)
a1 = Entry(root).grid(row=0, column=1)
password = Label(root, text="password").grid(row=1, column=0)
a2 = Entry(root).grid(row=1, column=1)

myButton = Button(root, text="Submit").grid(row=4,column=0)

root.mainloop()