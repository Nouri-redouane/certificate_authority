import tkinter as tk
from tkinter import ttk
from threading import Thread
from time import sleep

#"your cryptinh function here karim"
def crypt():
    global progressbar

    for i in range(0, 5):
        if (i==0):
            progressbar.configure(maximum=4)
        else:
            progressbar.step(0.99)
        sleep(1)


def crypt_button_clicked():
    Thread(target=crypt).start()


root = tk.Tk()
root.title("installing")

progressbar = ttk.Progressbar()
progressbar.place(x=100, y=150, width=400)
download_button = ttk.Button(text="YES! CRYPT MY FILES!!", command=crypt_button_clicked)
label = ttk.Label(text="install karim's game :) ? ", foreground="green", background="white", font=('Helvetica bold', 15))
download_button.place(x=250, y=100)
label.place(x=200, y=40)

root.geometry("600x250")
root.configure(background="white")
root.mainloop()
