# Ideas from: Fendy Lieanata, All rights reserved.

import hashlib
import os
import base64

dataTable = []

num_users = int(input("How many users do you want to create?"))

for i in range(num_users): 
    # create salt.  Fixed length (32 bytes) & random characters
    salt = os.urandom(32)
    username = input("Input a user name: ")
    password = input("Please Input a Password: ")

    # encode password into bytes and then hash.   
    hashed_password = hashlib.md5(password.encode() + salt)
    plaintext_salt = str(base64.b64encode(salt))

    dataTable.append([username, password, hashed_password.hexdigest(), plaintext_salt])

print('\n'.join(map(str, dataTable)))





