import os
import time
from __init__ import encrypt_file, decrypt_file
from key import newkeys, PrivateKey, PublicKey
from pkcs1 import (
    encrypt,
    decrypt,
    sign,
    verify,
    DecryptionError,
    VerificationError,
    find_signature_hash,
    sign_hash,
    compute_hash,
)

################## User input ##################
print('################## User input ##################')
# get the path of the folder to encrypt
#folder_path = input("Enter the path of the folder to encrypt: ")
folder_path = "D:\\flower.jpg"
# # get the path where the encrypted files will be stored
# folder_path_enc = input("Enter the path where the encrypted files will be stored: ")
#
# # get the path where the decrypted files will be stored
# folder_path_dec = input("Enter the path where the decrypted files will be stored: ")
#
# # get the path where the signed files will be stored
# folder_path_sig = input("Enter the path where the signed files will be stored: ")

print('######################################################')
################## Key generation ##################
print('################## Key generation ##################')

start = time.time()

# generate a keypair
(pubkey, privkey) = newkeys(1024)

end = time.time()

# log the public  and private keys
print("pubkey: %s %s" % (pubkey.n, pubkey.e))
print("privkey: %s %s" % (privkey.n, privkey.d))
print("Time to generate keys: %s" % (end - start)+" sec")

input("wanna continue?")

print('######################################################')
################## Encryption ##################
print('################## Encryption ##################')

start = time.time()
# get the list of files in the folder
# files_enc = os.listdir(folder_path)

# encrypt each file in the folder
# for file in files_enc:
#     encrypt_file(folder_path + '/' + file, pubkey)
encrypt_file(folder_path, pubkey)

end = time.time()
print("Time to encrypt files: %s" % (end - start)+" sec")
input("wanna continue?")
print('######################################################')
################## Decryption ##################
print('################## Decryption ##################')
start = time.time()

# files_dec = os.listdir(folder_path_enc)

# decrypt each file in the folder
# for file in files_dec:
#     #print("Decrypting file: " + file)
#     decrypt_file(folder_path_enc + '/' + file, folder_path_dec, privkey)

decrypt_file(folder_path, privkey)

end = time.time()

print("Time to decrypt files: %s" % (end - start)+" sec")

print('######################################################')