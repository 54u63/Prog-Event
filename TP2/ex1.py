from tkinter import *
from PIL import Image,ImageTk
from time import *
root=Tk()


main_canva=Canvas(root,bg="white",width=1000,height=1000)
main_canva.pack()


########################################CREATION DE L'OBJET POINTEUR############################
class pointeur:
    def __init__(self):
        self.state="None"
        self.menu_enable=False
        self.obj=[0,0]

########################################CREATION DE L'OBJET ROUTEUR#########################
class routeur:
    def __init__(self):
        """
        importe dans le constructeur l'image
        et créé positions
        """
        self.img=ImageTk.PhotoImage(Image.open("routeur.png"))
        self.size=32.5 
    def initialize(self,e,identifier):
        """
        initialise l'objet en l'important dans le canva
        à l'endroit ou l'utilisateur à cliqué.
        """
        self.posx=e.x
        self.posy=e.y
        self.id=identifier
        self.name="R"+str(self.id)
        self.rangeX=[self.posx-self.size,self.posx+self.size]
        self.rangeY=[self.posx-self.size,self.posy+self.size]
        self.routeur=main_canva.create_image(self.posx,self.posy,image=self.img)
        self.placeholder=main_canva.create_text(self.posx,self.posy+self.size,text=self.name)
    def change_name(self,name):
        self.name=name
        main_canva.itemconfigure(self.placeholder,text=self.name)


########################################CREATION DE LA CLASSE SWITCH###########################
class switch:
    def __init__(self):
        """
        importe dans le constructeur l'image
        et créé positions
        """
        self.img=ImageTk.PhotoImage(Image.open("switch.png"))
        self.size=32.5
    def initialize(self,e,identifier):
        """
        initialise l'objet en l'important dans le canva
        à l'endroit ou l'utilisateur à cliqué.
        """
        self.posx=e.x
        self.posy=e.y
        self.rangeX=[self.posx-self.size,self.posx+self.size]
        self.rangeY=[self.posx-self.size,self.posy+self.size]       
        self.id=identifier
        self.name="Sw"+str(self.id)
        self.switch=main_canva.create_image(self.posx,self.posy,image=self.img)
        self.placeholder=main_canva.create_text(self.posx,self.posy+self.size,text=self.name)


##########################################CREATION DE LA CLASSE CLIENT#########################

class client:
    def __init__(self):
        """
        importe dans le constructeur l'image
        et créé positions
        """       
        self.img=ImageTk.PhotoImage(Image.open("PC.png"))
        self.size=32.5
    def initialize(self,e,identifier):
        """
        initialise l'objet en l'important dans le canva
        à l'endroit ou l'utilisateur à cliqué.
        """
        self.posx=e.x
        self.posy=e.y
        self.rangeX=[self.posx-self.size,self.posx+self.size]
        self.rangeY=[self.posx-self.size,self.posy+self.size]        
        self.id=identifier
        self.name="C"+str(self.id)
        self.client=main_canva.create_image(self.posx,self.posy,image=self.img)
        self.placeholder=main_canva.create_text(self.posx,self.posy+self.size,text=self.name)

class menu_square:
    def __init__(self):
        self.size_x=100
        self.size_y=50
        self.text_1="renomer"
        self.text_2="icone"
    def init_menu(self,e):
        self.t1x=e.x+27
        self.t2x=e.x+18
        self.t1y=e.y+7
        self.t2y=e.y+20 
        self.rect=main_canva.create_rectangle(e.x,e.y,e.x+self.size_x,e.y+self.size_y,outline="black",fill="white")
        self.t1=main_canva.create_text(self.t1x,self.t1y,text=self.text_1)
        self.t2=main_canva.create_text(self.t2x,self.t2y,text=self.text_2)
    def destroy_menu(self):
        main_canva.delete(self.rect)
        main_canva.delete(self.t1)
        main_canva.delete(self.t2)
    def is_clicked(self,e):
        if e.x<self.t1x+(self.size_x-27) and e.x>self.t1x-27:
            if e.y<self.t1y+7 and e.y>self.t1y-7:
                global object_list
                rename(object_list[selector.obj[0]][selector.obj[1]])
                return 0
        if e.x<self.t2x+(self.size_x-18) and e.x>self.t2x-18:
            print("hi")
            if e.y<self.t2y+7 and e.x>self.t2y-7:
                print("icone")
                return 0

#########################################FONCTIONS####################################

def rename(name):
    main_canva.create_rectangle(200,200,800,800,outline="black",fill="white")
    textbox=Entry(root,text=name)
    label=Label(root,text="nom?")
    bouton=Button(root,text="valider",command=effective_rename(name))
    main_canva.create_window(500,400,window=label)
    main_canva.create_window(500,425,window=textbox)
    main_canva.create_window(500,450,window=bouton)
    print(name)

def effective_rename(name):
    global object_list 
    object_list[selector.obj[0]][selector.obj[1]].name=name

def create_routeur(e,object_list):
    new_routeur=routeur()
    new_routeur.initialize(e,len(object_list[0]))
    object_list[0].append(new_routeur)

def create_switch(e,object_list):
    new_switch=switch()
    new_switch.initialize(e,len(object_list[1]))
    object_list[1].append(new_switch)

def create_client(e,object_list):
    new_client=client()
    new_client.initialize(e,len(object_list[2]))
    object_list[2].append(new_client)

def menu(e):
    global menu_clicked
    menu_clicked=menu_square()
    menu_clicked.init_menu(e)
    selector.menu_enable=True
    return [e.x,e.y,e.x+100,e.y+50]


def destroy_menu():
    global menu_clicked
    menu_clicked.destroy_menu()
    selector.menu_enable=False


########################################VARIABLES####################################
selector=pointeur()
global object_list
object_list=[[],[],[]]
exit_button=Button(root,text="X",command=root.quit())
main_canva.create_window(925,10,window=exit_button)

#########################################CALLBACKS###############################
def click(e):
    global object_list
    if selector.state=="Routeur":
        create_routeur(e,object_list)
    elif selector.state=="Switch":
        create_switch(e,object_list)
    elif selector.state=="Client":
        create_client(e,object_list)
    elif selector.menu_enable==True and selector.state=="None":
        global menu_clicked
        menu_clicked.is_clicked(e)
    else:
        pass
        


def pressed(e):
    if e.char=="r":
        selector.state="Routeur"
    elif e.char=="s":
        selector.state="Switch"
    elif e.char=="c":
        selector.state="Client"
    elif e.char=="e":
        selector.state="None"
    else:
        pass

def rmb(e):
    global object_list
    test=0
    if selector.menu_enable is False:
        for i in range(len(object_list)):
            for j in range(len(object_list[i])):
                if e.x < object_list[i][j].rangeX[1] and e.x > object_list[i][j].rangeX[0]:
                    if e.y<object_list[i][j].rangeY[1] and e.y > object_list[i][j].rangeY[0]:
                        global menu_size
                        menu_size=menu(e)
                        selector.obj=[i,j]
                        return 0
    if selector.menu_enable is True:
        destroy_menu()    
   
root.bind("<KeyPress>",pressed)
root.bind("<Button-1>",click)
root.bind("<Button-2>",rmb)
root.bind("<Button-3>",rmb)
root.mainloop()
