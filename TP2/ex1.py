from tkinter import *
from PIL import Image,ImageTk
root=Tk()


main_canva=Canvas(root,bg="white",width=1000,height=1000)
main_canva.pack()


########################################CREATION DE L'OBJET POINTEUR############################
class pointeur:
    def __init__(self):
        self.state="None"



########################################CREATION DE L'OBJET ROUTEUR#########################
class routeur:
    def __init__(self):
        """
        importe dans le constructeur l'image
        et créé positions
        """
        self.img=ImageTk.PhotoImage(Image.open("routeur.png"))
        self.posx=0
        self.posy=0 
    def initialize(self,e,identifier):
        """
        initialise l'objet en l'important dans le canva
        à l'endroit ou l'utilisateur à cliqué.
        """
        self.posx=e.x
        self.posy=e.y
        self.id=identifier
        self.name="R"+str(self.id)
        self.routeur=main_canva.create_image(self.posx,self.posy,image=self.img)

########################################CREATION DE LA CLASSE SWITCH###########################
class switch:
    def __init__(self):
        """
        importe dans le constructeur l'image
        et créé positions
        """
        self.img=ImageTk.PhotoImage(Image.open("switch.png"))
        self.posx=0
        self.posy=0
    def initialize(self,e,identifier):
        """
        initialise l'objet en l'important dans le canva
        à l'endroit ou l'utilisateur à cliqué.
        """
        self.posx=e.x
        self.posy=e.y
        self.id=identifier
        self.name="Sw"+str(self.id)
        self.switch=main_canva.create_image(self.posx,self.posy,image=self.img)


##########################################CREATION DE LA CLASSE CLIENT#########################

class client:
    def __init__(self):
        """
        importe dans le constructeur l'image
        et créé positions
        """       
        self.img=ImageTk.PhotoImage(Image.open("PC.png"))
        self.posx=0
        self.posy=0
    def initialize(self,e,identifier):
        """
        initialise l'objet en l'important dans le canva
        à l'endroit ou l'utilisateur à cliqué.
        """
        self.posx=e.x
        self.posy=e.y
        self.id=identifier
        self.name="C"+str(self.id)
        self.client=main_canva.create_image(self.posx,self.posy,image=self.img)

#########################################FONCTIONS####################################

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




########################################VARIABLES####################################
selector=pointeur()
global object_list
object_list=[[],[],[]]



#########################################CALLBACKS###############################
def click(e):
    global object_list
    if selector.state=="Routeur":
        create_routeur(e,object_list)
    elif selector.state=="Switch":
        create_switch(e,object_list)
    elif selector.state=="Client":
        create_client(e,object_list)
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


root.bind("<KeyPress>",pressed)
root.bind("<Button-1>",click)
root.mainloop()
