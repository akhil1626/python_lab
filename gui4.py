from tkinter import *
root = Tk()
root.title("Traffic lights")
root.geometry("540x120")
var = StringVar()
var.set("white")
def setlight():
    L.config(text=f"you selected the {var.get()} light",bg=var.get())
button = Radiobutton(root,text="  Red  light  ",variable=var,value="Red",command=setlight,width=20).grid()
button = Radiobutton(root,text=" Green light",variable=var,value="Green",command=setlight,width=20).grid()
button = Radiobutton(root,text="Yellow light",variable=var,value="Yellow",command=setlight,width=20).grid()
L = Label(root,text="no light is selected",font="arias 14 bold",bg=var.get(),width=25)
L.grid(row=3,column=1)
root.mainloop()