from tkinter import *
from math import *
root=Tk()
root.geometry("360x360")
root.title("factorial")
def cal():
    temp=int(e.get())
    res=factorial(temp)
    r.config(text=res)
e=Entry(root)
e.pack(pady=15)
b=Button(root,text="Compute",font="arial 15 bold",bg="green",fg="white",command=cal)
b.pack()
r=Label(root,text="Result",font="arial  20  bold")
r.pack(pady=30)
root.mainloop()