from tkinter import *
from PIL import Image,ImageTk
root=Tk()


main_canva=Canvas(root,bg="white",width=1000,height=1000)
main_canva.pack()
class pointeur:
    def __init__(self):
        self.state="None"

class routeur:
    def __init___(self):
        self.img=ImageTk.PhotoImage(Image.open("routeur.jpg"))
        self.posx=0
        self.posy=0 
    def initialize(self,e,identifier):
        self.posx=e.x
        self.posy=e.y
        self.id=identifier
        self.routeur=main_canva.create_image(self.posx,self.posy,image=self.img)


class switch:
    def __init__(self):
        self.img=ImageTk.PhotoImage(Image.open("switch.png"))
        self.posx=0
        self.posy=0
    def initialize(self,e,identifier):
        self.posx=e.x
        self.posy=e.y
        self.id=identifier
        self.switch=main_canva.create_image(self.posx,self.posy,image=self.img)

class client:
    def __init__(self):
        self.img=ImageTk.PhotoImage(Image.open("PC.png"))
        self.posx=0
        self.posy=0
    def initialize(self,e,identifier):
        self.posx=e.x
        self.posy=e.y
        self.id=identifier
        self.client=main_canva.createimage(self.posx,self.posy,image=self.img)




selector=pointeur()


def pressed(e):
    if e.char=="r":
        selector.state="Routeur"
    elif e.char=="s":
        selector.state="Switch"
    elif e.char=="c":
        selector.state="Client"
    else:
        pass


root.bind("<KeyPress>",pressed)

root.mainloop()
