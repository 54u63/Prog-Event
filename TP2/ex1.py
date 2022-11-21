from tkinter import *
from PIL import Image,ImageTk
from time import *
from tkinter import ttk




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
class equipement():
    def __init__(self): 
        """
        importe dans le constructeur l'image
        et créé positions
        """
        self.size=35
    def initialize(self,e,identifier):
        """
        initialise l'objet en l'important dans le canva
        à l'endroit ou l'utilisateur à cliqué.
        """
        self.posx=e.x
        self.posy=e.y
        self.id=identifier
        self.name=self.prefix+str(self.id)
        self.rangeX=[e.x-self.size,e.x+self.size]
        self.rangeY=[e.y-self.size,e.y+self.size]
        self.object=main_canva.create_image(self.posx,self.posy,image=self.img)
        self.placeholder=main_canva.create_text(self.posx,self.posy+self.size,text=self.name)
    def change_name(self,name):
        self.name=name
        main_canva.itemconfigure(self.placeholder,text=self.name)

class routeur(equipement):
    def __init__(se lf):
        super().__init__()
        self.img=ImageTk.PhotoImage(Image.open("routeur.png"))
        self.prefix="R"
    def initialize(self,e,identifier):
        super().initialize(e,identifier)
    def change_name(self,name):
        super().change_name(name)


########################################CREATION DE LA CLASSE SWITCH###########################
class switch(equipement):
    def __init__(self):
        super().__init__()
        self.img=ImageTk.PhotoImage(Image.open("switch.png"))
        self.prefix="S"
    def initialize(self,e,identifier):
        super().initialize(e,identifier)
    def change_name(self,name):
        super().change_name(name)


#########################################CREATION DE LA CLASSE CLIENT#########################

class client(equipement):
    def __init__(self):
        super().__init__()
        self.img=ImageTk.PhotoImage(Image.open("PC.png"))
        self.prefix="C"
    def initialize(self,e,identifier):
        super().initialize(e,identifier)
    def change_name(self,name):
        super().change_name(name)


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
                rename(object_list[selector.obj[0]][selector.obj[1]].name)
                return 0
        if e.x<self.t2x+(self.size_x-18) and e.x>self.t2x-18:
            if e.y<self.t2y+7 and e.x>self.t2y-7:
                print("icone")
                return 0

#########################################FONCTIONS####################################

def rename(name):
    global object_list
    obj=object_list[selector.obj[0]][selector.obj[1]]
    def get_name():
        global menu_clicked
        obj.change_name(textbox.get())
        main_canva.delete(cute_labe)
        main_canva.delete(cute_txtbox)
        main_canva.delete(cute_button)
        main_canva.delete(cute_rectangle)
        menu_clicked.destroy_menu()
    cute_rectangle=main_canva.create_rectangle(200,200,800,800,outline="black",fill="white")
    textbox=Entry(root)
    label=Label(root,text="nom?")
    bouton=ttk.Button(root,text="valider",command=get_name)
    cute_labe=main_canva.create_window(500,400,window=label)
    cute_txtbox=main_canva.create_window(500,425,window=textbox)
    cut e_button=main_canva.create_window(500,450,window=bouton)

def icone():
    cute_rectangle=main_canva.create_rectangle(200,200,800,800,outline="black",fill="white")
    switch=main_canva.create_image(self.posx,self.posy,image="switch.png")
    routeur=main_canva.create_image(self.posx,self.posy,image="routeur.png")
    client=main_canva.create_image(self.posx,self.posy,image="PC.png")




def create_routeur(e,object_list):
    selector.state="None"
    new_routeur=routeur()
    new_routeur.initialize(e,len(object_list[0]))
    object_list[0].append(new_routeur)
    
def create_switch(e,object_list):
    selector.state="None"
    new_switch=switch() 
    new_switch.initialize(e,len(object_list[1]))
    object_list[1].append(new_switch)

def create_client(e,object_list):
    selector.state="None"
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
