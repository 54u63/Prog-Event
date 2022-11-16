from tkinter import *
from PIL import Image,ImageTk
from random import randint


root=Tk()

###############################création du damier##########################################
global size
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


###############################création de la classe dame######################################
class queen():
    def __init__(self,pos_queen):
        self.img=ImageTk.PhotoImage(Image.open("dame_resize.png"))
        a=randint(0,7)
        b=randint(0,7)
        while [a,b] in pos_queen:
            a=randint(0,7)
            b=randint(0,7)
        self.pos_x=a
        self.pos_y=b
        pos_queen.append([self.pos_x,self.pos_y])

    def aviable_case(self):
        case=[]
        for i in range(8):
            temp=[self.pos_x,i]
            if temp==[self.pos_x,pos_y]:
                pass
            else:
                case.append(temp)
        for i in range(8):
            temp=[i,self.pos_y]
            if temp==[self.pos_x,self.pos_y]:
                pass
            else:
                case.append(temp)
        return case
    
    def create_queen(self,size):
        pos_x=self.pos_x*size+size/2
        pos_y=self.pos_y*size+size/2
        self.cases=aviable_case()
        self.queen=main_canva.create_image(pos_x,pos_y,image=self.img)
#################################intialisation des 8 dames#####################################

def create_8_queens(size):
    pos_queen=[]
    queens=[]
    for i in range(8):
        current_queen=queen(pos_queen)
        current_queen.create_queen(size)
        queens.append(current_queen)
    return pos_queen,queens

global queen_pos
global queens
queens_list=create_8_queens(size)
queen_pos=queens_list[0]
queens=queens_list[1]
###################################callbacks events############################################
def mouse_pos_checker(e):
    global queen_pos
    global size
    pos=[int((e.x-(e.x%size))/size),int((e.y-(e.y%size))/size)]
    out=8
    for i in range(len(queen_pos)):
        if pos==queen_pos[i]:
            out=i
        else:
            pass
    return out
def move(e):
    mouse_case=mouse_pos_checker(e)
    if mouse_case==8:
        pass
    else:
        global queen
        cu_queen=queen[mouse_case]
        print(cu_queen.case)
        

def release(e):
    print("")
label=Label(root,text="")
label.pack()

root.bind("<B1-Motion>",move)
root.bind("<ButtonRelease-1>",release)
main_canva.pack()
root.mainloop()
