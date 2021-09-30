from tkinter import *
root = Tk()
def myClick():
    myLabel = Label(root, text="Buttons")
    myLabel.pack()


myButton = Button(root, text="Hello", padx="50px", command=myClick,fg="green",bg="yellow")
# disable
# myButton = Button(root, text="Hello", state="Disable")
myButton.pack()
root.mainloop()