from tkinter import *
from PIL import Image,ImageTk,ImageGrab

root=Tk()
canva=Canvas(root,bg="white",width=1200,height=1200)
canva.pack()
global img
img=ImageTk.PhotoImage(Image.open("dame_resize.png"))
global pos
pos=[200,200]
global image
my_image=canva.create_image(pos[0],pos[1],image=img)


def move(e):
    global img
    global my_image
    global pos
    canva.move(my_image,e.x,e.y)

def say_hi(e):
    print("hi")

canva.bind("<Return>",say_hi)

root.mainloop()
