import os
from tkinter import *


def date_validity():
    tp3.place(x=450, y=250, width=95, height=30)
    ent.place(x=300, y=250, width=95, height=30)
    lbl.place(x=50, y=250, width=250, height=30)

def generate_txt_cert():
    os.system(r'cmd /c "openssl x509 -in C:\Users\hp\Documents\PythonScripts\cry\entity.crt -text -noout > C:\Users\hp\Documents\PythonScripts\cry\certificate.txt"')

def verify():
    global date
    t = date.get()
    #date represente le temps de validite, par exemple si date==60, cad est ce que le certificat est valide apres 60 secondes
    x = os.system(f'cmd /c "openssl x509 -in C:\\Users\\hp\\Documents\\PythonScripts\\cry\\entity.crt -noout -checkend {t}"') 
    if x == 0:
        lbl_valid = Label(fenetre, text=f"Certificate will not expire in {t} secondes",
                 font=("Myriad Arabic", 10), bg="#f5f0e1")
        lbl_valid.place(x=250, y=300, width=250, height=30)
    else:
        lbl_not_valid = Label(fenetre, text=f"Certificate will expire in {t}secondes",
                 font=("Myriad Arabic", 10), bg="#f5f0e1")
        lbl_not_valid.place(x=250, y=300, width=250, height=30)



fenetre = Tk()
# info sur la fenetre
fenetre.title("validity")
fenetre.geometry('700x500')
fenetre.resizable(False, False)
title = Label(fenetre, text='validity', fg='white', bg='#1e3d59')
title.config(font=('times', 20, 'bold'))
title.pack(fill=X)


# string var
date = IntVar()
# les bouttons

tp1 = Button(fenetre, text='generate', command=generate_txt_cert,
             fg='#f5f0e1', bg='#1e3d59')
tp1.config(font=('times', 16, 'bold'))
tp1.place(x=300, y=100, width=95, height=30)

tp2 = Button(fenetre, text='validity', command=date_validity,
             fg='#f5f0e1', bg='#1e3d59')
tp2.config(font=('times', 16, 'bold'))
tp2.place(x=300, y=180, width=95, height=30)

tp3 = Button(fenetre, text='verify', command=verify,
             fg='#f5f0e1', bg='#1e3d59')
tp3.config(font=('times', 16, 'bold'))


# les entr
ent = Entry(fenetre, bd="1", justify="center", textvariable=date)

# les labels
lbl = Label(fenetre, text="Entrer la durée de validite (en secondes)",
                 font=("Myriad Arabic", 10), bg="#f5f0e1")


fenetre.mainloop()
