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
    def __init___(self):
        """
        importe dans le constructeur l'image
        et créé positions
        """
        self.img=ImageTk.PhotoImage(Image.open("routeur.jpg"))
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
        self.client=main_canva.createimage(self.posx,self.posy,image=self.img)

#########################################FONCTIONS####################################

def create_routeur():
    print("routeur")

def create_switch():
    print("switch")

def create_client():
    print("client")




########################################VARIABLES####################################
selector=pointeur()
object_list=[]



#########################################CALLBACKS###############################
def click(e):
    if selector.state=="Routeur":
        create_routeur()
    elif selector.state=="Switch":
        create_switch()
    elif selector.state=="Client":
        create_client()
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
