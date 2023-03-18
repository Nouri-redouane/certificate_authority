import os
from tkinter import *


def date_validity():
    tp3.place(x=450, y=250, width=95, height=30)
    ent.place(x=300, y=250, width=95, height=30)
    lbl.place(x=100, y=250, width=140, height=30)

def generate_txt_cert():
    os.system(r'cmd /c "openssl x509 -in C:\Users\hp\Documents\PythonScripts\cry\entity.crt -text -noout > C:\Users\hp\Documents\PythonScripts\cry\certificate.txt"')

def verify():
    global date
    #date represente le temps de validite, par exemple si date==60, cad est ce que le certificat est valide apres 60 secondes
    os.system(f'cmd /c "openssl x509 -in C:\\Users\\hp\\Documents\\PythonScripts\\cry\\entity.crt -noout -checkend {date}"') 
    print(f"in {date} secondes")



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
lbl = Label(fenetre, text="entre la duree de validite",
                 font=("Myriad Arabic", 10), bg="#f5f0e1")

fenetre.mainloop()
