from tkinter import *

root=Tk()
def validation_email():
    entry=email_input.get()
    validation=0
    matched_char=["@","."]
    unmatched_char=[" "]
    for i in range(len(matched_char)):
        if matched_char[i] in entry:
            validation+=1
    for i in range(len(unmatched_char)):
        if unmatched_char[i] not in entry:
            validation+=1
    ####button###
    if validation<3:
        b1["state"]="disabled"
    if validation==3:
        b1["state"]="normal"




email_input=StringVar()
email_input.trace("w",lambda name, index, mode, email_input=email_input: validation_email())

text_top=Label(root,text="Veuillez entrer votre Email").grid(sticky="NWNE")
email_entry=Entry(root,text=email_input).grid(sticky="EW")
b1=Button(root,text="valider")
b1.grid(sticky="SE")
b1["state"]="disabled"
root.mainloop()
