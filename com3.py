# importing everything from tkinter
from tkinter import *
 
# create gui window
Main_window = Tk()
 
# set the configuration
# of the window
Main_window.geometry("220x100")
 


# define a function
# for setting the new text
def java():
    num=int(number.get())+2
    number.set(str(num))
 
# define a function
# for setting the new text
def python():
    num=int(number.get())-2
    number.set(str(num))
 
 
 
# create a Button widget and attached  
# with java function  
btn_1 = Button(Main_window,
               text = "+",
               command = java)
 
# create a Button widget and attached  
# with python function
btn_2 = Button(Main_window,
               text = "-",
               command = python)
 
# create a StringVar class
number= StringVar()
 
# set the text
number.set("0")
 
# create a label widget
my_label = Label(Main_window,
                 textvariable = number)
 
 
# place widgets into
# the gui window
btn_1.pack()
btn_2.pack()
my_label.pack()
 
# Start the GUI 
Main_window.mainloop()
