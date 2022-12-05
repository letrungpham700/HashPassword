

import hashlib, binascii, os
import sys

# Create a hashed password
def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha512(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

# # Check hashed password validity
# def verify_password(stored_password, provided_password):
#     """Verify a stored password against one provided by user"""
#     salt = stored_password[:64]
#     stored_password = stored_password[64:]
#     pwdhash = hashlib.pbkdf2_hmac('sha512',
#                                   provided_password.encode('utf-8'),
#                                   salt.encode('ascii'),
#                                   100000)
#     pwdhash = binascii.hexlify(pwdhash).decode('ascii')
#     return pwdhash == stored_password

# # Create password checking prompt
# def passwordChecker(initialPassword):
#   password = initialPassword
#   storedPassowrd = hash_password(password)
#   while(1):
#       passowrd_input = input("Enter your computer password: ")
#       checker = verify_password(storedPassowrd, passowrd_input)
#       if checker:
#           print("Passwords match")
#           break
#       else:
#           print("Password incorrect, try again.")
          
# Run program
initialPassword = input("Enter password to encrypt: ")
print(hash_password(initialPassword))

# EOF

import hashlib

l = ["ltpham", "dktich"]

def check_user(h):
    for i in l:
        if h == hashlib.sha512(i.encode('utf-8')).hexdigest():
            return i


print(check_user(hashlib.sha512(l[2].encode('utf-8')).hexdigest()))

# import crypt

# def CryptSHA(password):
#     turn = crypt.crypt(password, crypt.mksalt(crypt.METHOD_SHA512))
#     return turn


# def HashPass():
#     DirFile = 'Password.txt'
#     File = open(DirFile, 'r')
#     Lines = File.readlines()
#     count = 0
#     for Pass in Lines:
#         count += 1
#         PassData = Pass.strip()
#         hashpass = CryptSHA(PassData)
#         print(PassData+':'+hashpass)

# if __name__ == "__main__":
#     HashPass()


import crypt
import os
import string

try:  # 3.6 or above
    from secrets import choice as randchoice
except ImportError:
    from random import SystemRandom
    randchoice = SystemRandom().choice

id = ['1','2','2a','2x','2y','3','5','6','7','md5','sha1','gy','y']    

import crypt
import os
# PASS='ltpham@2020'
# SALT='$y$j9T$F31F/jItUvvjOv6IBFNea/$'
# perl -le 'print crypt($ENV{PASS}, $ENV{SALT})'
# python -c 'import crypt, os; print(crypt.crypt(os.getenv("PASS"), os.getenv("SALT")))'
hash = crypt.crypt(os.getenv("ltpham@2020"), os.getenv("$y$j9T$DHb8G5deVnOaO2cu3Xn.b.$"))
print(hash)


import crypt
hash = crypt.crypt('ltpham@2020', '$y$j9T$' + 'DHb8G5deVnOaO2cu3Xn.b.')
print(hash)
# for x in id:
#   print(type(x))
#   print(x)

import sys
import subprocess
def changePass (username , password) :
    shadow = open("/etc/shadow" , "r")
    if shadow :
        lines = shadow.readlines()
        shadow.close()
        for line in lines :
            if line.find(username) == 0 :
                tempLine = line
                lines.remove(line)
                tempLine = tempLine.split(":")
                # tempLine[1] = subprocess.getoutput("python -c 'import crypt; print crypt.crypt(\"%s\", \"$6$AWI-CO$\")'" %(password))
                lines.append(str.join(":",tempLine))
        shadow = open("/etc/shadow" , "w")
        shadow.write(str.join("",lines))
        shadow.close()

    else :
        print("file '/etc/shadow' is not open !")

import crypt
def sha512_crypt(password, salt=None, rounds=None):
    # if salt is None:
    salt = 'hrEEvwUBF9x6rzbC'

    prefix = '$6$'
    if rounds is not None:
        rounds = max(1000, min(999999999, rounds or 5000))
        prefix += 'rounds={0}$'.format(rounds)
    return crypt.crypt(password, prefix + salt)
    
def yes_crypt(password, salt=None, rounds=None):
    # if salt is None:
    # salt = 'DHb8G5deVnOaO2cu3Xn.b.'

    # prefix = '$y$j9T$'
    # if rounds is not None:
    #     rounds = max(1000, min(999999999, rounds or 5000))
    #     prefix += 'rounds={0}$'.format(rounds)
    # return crypt.crypt(password, prefix + salt)
    DirFile = 'Salt.txt'
    File = open(DirFile, 'r')
    Lines = File.readlines()
    count = 0
    for Salt in Lines:
        count += 1
        SaltData = Salt.strip()
        prefix = '$y$j9T$'
        if rounds is not None:
            rounds = max(1000, min(999999999, rounds or 5000))
            prefix += 'rounds={0}$'.format(rounds)
            hashyes = crypt.crypt(password, prefix + SaltData)
            print("Yescrypt - "+password+" : "+hashyes)
        # return crypt.crypt(password, prefix + SaltData)

    
def CheckHash():
    DirFile = 'Password.txt'
    File = open(DirFile, 'r')
    Lines = File.readlines()
    count = 0
    for Pass in Lines:
        count += 1
        PassData = Pass.strip()
        hashpass = sha512_crypt(PassData)
        hashyes = yes_crypt(PassData)
        print("SHA512 - "+PassData+':'+hashpass)
        print(hashyes)


if __name__ == "__main__":
    CheckHash()