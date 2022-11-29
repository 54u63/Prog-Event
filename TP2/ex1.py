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
        self.icone=False
        self.obj=[0,0]
        self.rename=False
        self.control=False
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
    def __init__(self,images):
        super().__init__()
        self.prefix="R"
        self.img=images[0]
        self.port=2
        self.port_aviable=2
    def initialize(self,e,identifier):
        super().initialize(e,identifier)
    def change_name(self,name):
        super().change_name(name)
########################################CREATION DE LA CLASSE SWITCH###########################
class switch(equipement):
    def __init__(self,images):
        super().__init__()
        self.prefix="S"
        self.img=images[1]
        self.port=2
        self.port_aviable=2
    def initialize(self,e,identifier):
        super().initialize(e,identifier)
    def change_name(self,name):
        super().change_name(name)
#########################################CREATION DE LA CLASSE CLIENT#########################
class client(equipement):
    def __init__(self,images):
        super().__init__()
        self.prefix="C"
        self.img=images[2]
        self.port=1
        self.port_aviable=1
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
            if e.y<self.t2y+7 and e.y>self.t2y-7:
                icone()
                return 0

class link():
    def __init__(self,start,end):
        self.start=[start.posx,start.posy]
        self.end=[end.posx,end.posy]
        self.obj=[start,end]
    def create_link(self):
        self.line=main_canva.create_line(self.start[0],self.start[1],self.end[0],self.end[1],fill="black",width=3)
        return self.line

#########################################FONCTIONS####################################
def rename(name):
    global object_list
    selector.rename=True
    obj=object_list[selector.obj[0]][selector.obj[1]]
    def get_name():
        selector.rename=False
        global menu_clicked
        obj.change_name(textbox.get())
        for i in range(len(rename_menu)):
            main_canva.delete(rename_menu[i])
        menu_clicked.destroy_menu()
    cute_rectangle=main_canva.create_rectangle(200,200,800,800,outline="black",fill="white")
    textbox=Entry(root)
    label=Label(root,text="nom?")
    bouton=ttk.Button(root,text="valider",command=get_name)
    cute_labe=main_canva.create_window(500,400,window=label)
    cute_txtbox=main_canva.create_window(500,425,window=textbox)
    cute_button=main_canva.create_window(500,450,window=bouton)
    global rename_menu
    rename_menu=[cute_labe,cute_txtbox,cute_rectangle,cute_button]

def icone():
    global object_list
    obj=object_list[selector.obj[0]][selector.obj[1]]
    global images
    pref_list=["R","S","C"]
    index=pref_list.index(obj.prefix)
    pref_used=""
    if index==len(pref_list)-1:
        pref_used+=pref_list[0]
    else:
        pref_used+=pref_list[index+1]
    if pref_used=="R":
        main_canva.itemconfigure(obj.object,image=images[0])
    if pref_used=="C":
        main_canva.itemconfigure(obj.object,image=images[2])
    if pref_used=="S":
        main_canva.itemconfigure(obj.object,image=images[1])
    else:
        pass
    global menu_clicked
    menu_clicked.destroy_menu()
    obj.prefix=pref_used


def create_routeur(e,object_list,images):
    selector.state="None" 
    new_routeur=routeur(images)
    new_routeur.initialize(e,len(object_list[0]))
    object_list[0].append(new_routeur) 
    
def create_switch(e,object_list,images):
    selector.state="None" 
    new_switch=switch(images)
    new_switch.initialize(e,len(object_list[1]))
    object_list[1].append(new_switch)

def create_client(e,object_list,images):
    selector.state="None" 
    new_client=client(images)
    new_client.initialize(e,len(object_list[2]))
    object_list[2].append(new_client)

def menu(e):
    global menu_clicked
    menu_clicked=menu_square()
    menu_clicked.init_menu(e)
    selector.menu_enable=True
    return [e.x,e.y,e.x+ 100,e.y+50]

def destroy_menu():
    global menu_clicked 
    menu_clicked.destroy_menu()
    selector.menu_enable=False

def two_obj(numb_obj,e):
    if len(numb_obj)<2:
        global object_list
        for i in range(len(object_list)):
            for j in range(len(object_list[i])):
                if e.x < object_list[i][j].rangeX[1] and e.x > object_list[i][j].rangeX[0]:
                    if e.y<object_list[i][j].rangeY[1] and e.y > object_list[i][j].rangeY[0]:
                        return object_list[i][j]                 
    else:
        return 0

def create_link(obj_list):
    global link_list
    if obj_list[0].port_aviable>0:
        if obj_list[1].port_aviable>0:
            current_link=link(obj_list[0],obj_list[1])
            current_link.create_link()
            link_list.append(current_link)
            obj_list[0].port_aviable-=1
            obj_list[1].port_aviable-=1
            return 0
    else:
        print("pas assez de port sur la machine!")
        return 1

def draw(e):
    line_drawed=None
    if main_canva.old_coords:
        p2_x,p2_y= main_canva.old_coords
        line_drawed=main_canva.create_line(p2_x,p2_y,e.x,e.y,width=3,fill="black")
    main_canva.old_coords=e.x,e.y
    return line_drawed
    
########################################VARIABLES####################################
selector=pointeur()
main_canva.old_coords=None
global link_list
link_list=[]
global object_list
object_list=[[],[],[]]
exit_button=Button(root,text="X",command=root.quit())
main_canva.create_window(925,10,window=exit_button)
global images
images=[ImageTk.PhotoImage(Image.open("routeur.png")),
        ImageTk.PhotoImage(Image.open("switch.png")),
        ImageTk.PhotoImage(Image.open("PC.png"))]
global linked_obj
linked_obj=[]
global draw_list
draw_list=[]
global drawing
drawing=[]
#########################################CALLBACKS###############################
def click(e):
    global object_list
    if selector.state=="Routeur":
        create_routeur(e,object_list,images)
    elif selector.state=="Switch":
        create_switch(e,object_list,images)
    elif selector.state=="Client":
        create_client(e,object_list,images)
    elif selector.menu_enable==True and selector.state=="None":
        global menu_clicked
        menu_clicked.is_clicked(e)
    elif selector.state=="line":
        global linked_obj
        re=two_obj(linked_obj,e)
        if re==0:
            create_link(linked_obj)
            linked_obj=[]
        else:
            linked_obj.append(re)
        
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
        main_canva.old_coords=None
    elif e.char=="l":
        selector.state="line"
    elif e.char=="d":
        selector.state="draw"
    else:
        pass
    print(selector.state)
    print(selector.control)
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

def escape(e):
    if selector.menu_enable==True:
        global menu_clicked
        menu_clicked.destroy_menu()
        selector.menu_enable==False
    if selector.rename==True:
        global rename_menu
        for i in range(len(rename_menu)):
            main_canva.delete(rename_menu[i])
    selector.state="None"
    main_canva.old_coords=None
    global drawing
    global draw_list
    draw_list.append(drawing)
    print(draw_list)

def motion(e):
    if selector.state=="draw":
        global drawing
        if selector.control==False:
            drawing.append(draw(e))

def control(e):
    selector.control=True

def release(e):
    if selector.control==False:
        pass
    else:
        selector.control=False

root.bind("<KeyPress>",pressed)
root.bind("<Button-1>",click)
root.bind("<Button-2>",rmb)
root.bind("<Button-3>",rmb)
root.bind("<Escape>",escape)
root.bind("<B1-Motion>",motion)
root.bind("<KeyRelease>",release)
root.bind("<Control_L>",control)
root.mainloop()
