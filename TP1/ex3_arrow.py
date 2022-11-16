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
        self.id=0
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

class case:
    def __init__(self):
        global size
        self.x=0
        self.y=0
        self.color="yellow"

    def init_rect():
        main_canva.create_rectangle(0,0,size,size,fill=self.color)

    def get_current_color(self):
        pos=(main_canva.winfo_rootx()+self.x*size,main_canva.winfo_rooty()+self.y*size)
        pos=(pos[0]+2,pos[1]+2,pos[0]+3,pos[1]+3)
        current_color=ImageGrab.grab(pos).getpixel((0,0))
        if current_color==(255,255,255):
            self.current_color="white"
        if current_color==(0,0,0):
            self.current_color="black"
        else:
            self.current_color="queen"
    def move(self,direction):
        if direction=="left":
            main_canva.create_rectangle(self.x,self.y,self.x+size,self.y+size,fill=self.current_color)
            self.x-=size
            main_canva.create_rectangle(self.x,self.y,self.x+size,self.y+size,fill=self.color)
        if direction=="right":
            main_canva.create_rectangle(self.x,self.y,self.x+size,self.y+size,fill=self.current_color)
            self.x+=size
            main_canva.create_rectangle(self.x,self.y,self.x+size,self.y+size,fill=self.color)
        
        if direction=="up":
            main_canva.create_rectangle(self.x,self.y,self.x+size,self.y+size,fill=self.current_color)
            self.y+=size
            main_canva.create_rectangle(self.x,self.y,self.x+size,self.y+size,fill=self.color)

        if direction=="down":
            main_canva.create_rectangle(self.x,self.y,self.x+size,self.y+size,fill=self.current_color)
            self.y-=size
            main_canva.create_rectangle(self.x,self.y,self.x+size,self.y+size,fill=self.color)


#################################intialisation des 8 dames#####################################



def create_8_queens(size):
    pos_queen=[]    
    queens=[]
    for i in range(8):
        current_queen=queen(pos_queen)
        current_queen.create_queen(size)
        current_queen.aviable_case()
        current_queen.id=i
        queens.append(current_queen)
    return pos_queen,queens 

selecteur=case()
selecteur.get_current_color()
selecteur.init_rect()
def move_left(e):
    selecteur.get_current_color()
    if selecteur.current_color!="queen":
        selecteur.move("left")

def move_right(e):
    print("here")
    selecteur.get_current_color()
    print(selecteur.current_color)
    if selecteur.current_color!="queen":
        selecteur.move("right")

def move_down(e):
    selecteur.get_current_color()
    if selecteur.current_color!="queen":
        selecteur.move("down")

def move_up(e):
    selecteur.get_current_color()
    if selecteur.current_color!="queen":
        selecteur.move("up")    

global queen_pos
global queens
queens_list=create_8_queens(size)
queen_pos=queens_list[0]
queens=queens_list[1]


###############################fonctions########################################################

def color_aviable(queen,pos_queens,size,color_tab=[]):
    aviablepos=queen.case
    out=1
    if queen.show_case==False:
        color_tab=[]
        for i in range(len(aviablepos)):
            posx_square=aviablepos[i][0]*size
            posy_square=aviablepos[i][1]*size
            if aviablepos[i] in pos_queens:
                main_canva.create_rectangle(posx_square,posy_square,posx_square+size,posy_square+size,fill="red")
                color_tab.append("queen")
            else:
                pos=(main_canva.winfo_rootx()+posx_square+2,main_canva.winfo_rooty()+posy_square+2,main_canva.winfo_rootx()+posx_square+3,main_canva.winfo_rooty()+posy_square+3)
                color=ImageGrab.grab(pos).getpixel((0,0))
                if color==(255,255,255):
                    color_tab.append("white")
                if color==(0,0,0):
                    color_tab.append("black")
                main_canva.create_rectangle(posx_square,posy_square,posx_square+size,posy_square+size,fill="green")
        
        return True,color_tab

    if queen.show_case==True:
        for i in range(len(aviablepos)):
            posx_square=aviablepos[i][0]*size
            posy_square=aviablepos[i][1]*size
            if aviablepos[i] in pos_queens:
                main_canva.create_image(posx_square+size/2,posy_square+size/2,image=queen.img)
            else:
                main_canva.create_rectangle(posx_square,posy_square,posx_square+size,posy_square+size,fill=color_tab[i])
        return False,color_tab

def move_queen(queen,e):
    global size
    global color_tab
    mouse_case=[int((e.x-(e.x%size))/size),int((e.y-(e.y)%size)/size)]
    if mouse_case in queen.case:
        pos=0
        for i in range(len(queen.case)):
            if mouse_case==queen.case:
                pos+=i
        if color_tab[pos]=="queen":
            print("salam")
            return 1
        move=[mouse_case[0]*size+size/2,mouse_case[1]*size+size/2]
        main_canva.create_image(move[0],move[1],image=queen.img)
    else:
        print("bye")


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

global color_tab
color_tab=[]
global cu_queen
cu_queen=queens[0]
def move(e):
    print("hi")
    mouse_case=mouse_pos_checker(e)
    global queens
    global queen_pos
    global size
    global color_tab
    global cu_queen
    if mouse_case<8 and queens[mouse_case].show_case==False:
        cu_queen=queens[mouse_case]
        out=color_aviable(cu_queen,queen_pos,size)
        cu_queen.show_case=out[0]
        color_tab=out[1]
    else:
        move_queen(cu_queen,e)
        out=color_aviable(cu_queen,queen_pos,size,color_tab=color_tab)
        cu_queen.show_case=out[0]


def release(e):
    pass


root.bind("<Left>",move_left)
root.bind("<Right>",move_right)
root.bind("<Up>",move_up)
root.bind("<Down>",move_down)


main_canva.pack()
root.mainloop()
