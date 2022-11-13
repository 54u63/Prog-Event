from tkinter import *
from PIL import Image,ImageTk,ImageGrab
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
        self.show_case=False
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
            if temp==[self.pos_x,self.pos_y]:
                pass
            else:
                case.append(temp)
        for i in range(8):
            temp=[i,self.pos_y]
            if temp==[self.pos_x,self.pos_y]:
                pass
            else:
                case.append(temp)
        self.case=case
        for i in range(8):                                      #
            posx=self.pos_x+i                                   #
            posy=self.pos_y+i                                   #
            if posx>7 or posx<0 or posy<0 or posy>7:            #
                pass                                            #
            else:                                               # très laid et peu efficace
                if [posx,posy]!=[self.pos_x,self.pos_y]:        # pour l'intant ça fonctionne mais à voir
                    case.append([posx,posy])                    #
                else:                                           #
                    pass                                        #
 
        for i in range(8):
            posx=self.pos_x-i
            posy=self.pos_y-i
            if posx>7 or posx<0 or posy<0 or posy>7:
                pass
            else:
                if [posx,posy]!=[self.pos_x,self.pos_y]:
                    case.append([posx,posy])
                else:
                    pass

        for i in range(8):
            posx=self.pos_x+i
            posy=self.pos_y-i
            if posx>7 or posx<0 or posy<0 or posy>7:
                pass
            else:
                if [posx,posy]!=[self.pos_x,self.pos_y]:
                    case.append([posx,posy])
                else:
                    pass
        for i in range(8):
            posx=self.pos_x-i
            posy=self.pos_y+i
            if posx>7 or posx<0 or posy<0 or posy>7:
                pass
            else:
                if [posx,posy]!=[self.pos_x,self.pos_y]:
                    case.append([posx,posy])
                else:
                    pass


    def create_queen(self,size):
        pos_x=self.pos_x*size+size/2
        pos_y=self.pos_y*size+size/2
        self.queen=main_canva.create_image(pos_x,pos_y,image=self.img)
#################################intialisation des 8 dames#####################################



def create_8_queens(size):
    pos_queen=[]
    queens=[]
    for i in range(8):
        current_queen=queen(pos_queen)
        current_queen.create_queen(size)
        current_queen.aviable_case()
        queens.append(current_queen)
    return pos_queen,queens

global queen_pos
global queens
queens_list=create_8_queens(size)
queen_pos=queens_list[0]
queens=queens_list[1]


###############################fonctions########################################################

def color_aviable(queen,pos_queens,size):
    aviablepos=queen.case
    out=1
    if queen.show_case==False:
        color_tab=[]
        for i in range(len(aviablepos)):
            posx_square=aviablepos[i][0]*size
            posy_square=aviablepos[i][1]*size
            if aviablepos[i] in pos_queens:
                posx_square=aviablepos[i][0]*size
                posy_square=aviablepos[i][1]*size
                main_canva.create_rectangle(posx_square,posy_square,posx_square+size,posy_square+size,fill="red")
            else:
                main_canva.create_rectangle(posx_square,posy_square,posx_square+size,posy_square+size,fill="green")
        return True

    if queen.show_case==True:
        for i in range(len(aviablepos)):
            print(main_canva.winfo_rootx)
            print(ImageGrab.grab((main_canva.winfo_rootx,main_canva.winfo_rooty)))
            posx_square=aviablepos[i][0]*size
            posy_square=aviablepos[i][1]*size
            if aviablepos[i] in pos_queens:
                main_canva.create_image(posx_square+size/2,posy_square+size/2,image=queen.img)
            else:
                if aviablepos[i][0]%2==0 and aviablepos[i][1]%2==0:
                    main_canva.create_rectangle(posx_square,posy_square,posx_square+size,posy_square+size,fill="white")
                else:
                    main_canva.create_rectangle(posx_square,posy_square,posx_square+size,posy_square+size,fill="black")
        return False



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
        color_refresh
    else:
        global queens
        global queen_pos
        global size
        queens[mouse_case].show_case=color_aviable(queens[mouse_case],queen_pos,size)
        

def release(e):
    print("")
label=Label(root,text="")
label.pack()

root.bind("<Button-1>",move)
root.bind("<ButtonRelease-1>",release)
main_canva.pack()
root.mainloop()
