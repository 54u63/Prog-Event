from tkinter import *
from PIL import Image,ImageTk
 


root=Tk()

###############################création du damier##########################################
size=50
main_canva=Canvas(root,bg="white",width=400,height=400)
def white_start(i):
    for j in range(8):
        if j%2==0:
            main_canva.create_rectangle(i*size,j*size,i*size+size,j*size+size,fill="white")
        if j%2==1:
            main_canva.create_rectangle(i*size,j*size,i*size+size,j*size+size,fill="black")

def black_start(i):
    for j in range(8):
        if j%2==1:
            main_canva.create_rectangle(i*size,j*size,i*size+size,j*size+size,fill="white")
        if j%2==0:
            main_canva.create_rectangle(i*size,j*size,i*size+size,j*size+size,fill="black")


for i in range(8):
    if i%2==0:
        white_start(i)
    if i%2==1:
        black_start(i)


#############################importation de l'image##########################################
img= ImageTk.PhotoImage(Image.open("dame_resize.png"))
dame=main_canva.create_image(25,25,image=img)

###############################déplacement de la dame######################################
def left(e):
    main_canva.move(dame,-size,0)
def right(e):
    main_canva.move(dame,size,0)
def down(e):
    main_canva.move(dame,0,size)
def up(e):
    main_canva.move(dame,0,-size)


root.bind("<Right>",right)
root.bind("<Left>",left)
root.bind("<Down>",down)
root.bind("<Up>",up)


main_canva.pack()
root.mainloop()
