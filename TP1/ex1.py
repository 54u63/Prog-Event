from tkinter import *


root=Tk()
def increment():
    num=int(number.get())+2
    number.set(str(num))

def decrement():
    num=int(number.get())-2
    number.set(str(num))

btn_plus=Button(root,text="+",command=increment)
btn_moins=Button(root,text="-",command=decrement)

number=StringVar()
number.set("0")

placeholder=Label(root,textvariable=number)

btn_plus.pack()
btn_moins.pack()
placeholder.pack()

root.mainloop()
