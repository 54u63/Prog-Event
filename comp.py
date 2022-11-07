from tkinter import *
from tkinter import ttk




#######################Creation de frame#####################"""
root=Tk()
root.title("test.frame")
"""
#######################Fonctions et variables globales#############
number=StringVar()
number.set("0")
num=int(number.get())
def increment(num):
    num+=2
    number.set(str(num))

######################placement des widgets##########################
#numholder=ttk.Label(frame,text=number)
#incr_button=ttk.Button(frame,text="+",command=increment(num))
"""
quit_button=ttk.Button(root,text="quit",command=root.destroy)

#numholder.pack()
#incr_button.pack()
quit_button.pack
root.mainloop()

