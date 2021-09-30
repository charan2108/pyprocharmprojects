from tkinter import *

root = Tk()
e = Entry(root, width=25,borderwidth=5)
e.pack()
e.get()
e.insert(0, "Enter your name:")
def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text="Hello")
    myLabel.pack()
   
myButton = Button(root, text="Enter Name", command=myClick)
myButton.pack()
root.mainloop()