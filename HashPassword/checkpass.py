import crypt
import string
import datetime
import subprocess
from pathlib import Path
import pathlib

from HashPassword.time import TimeYesterday, Today
#==================================================================

def TotalUser():
    day_scan = Today()
    with open('/etc/passwd') as file:
        for line in file:
            if '/bin/bash' in line:
                total_user = line.split(":")[0]
                wlog = open("ScanUser-"+day_scan+".txt","a+")
                wlog.write(total_user+"\n")
    RemoveFileOld()
    return wlog

def RemoveFileOld():
    yesterday = TimeYesterday()
    file = pathlib.Path("ScanUser-"+yesterday+".txt")
    if file.exists():
        subprocess.call(["rm", "ScanUser-"+yesterday+".txt"])
    else:
        pass

#==================================================================

#==================================================================
def sha512_crypt(password, rounds=None):
    DirFile = 'Salt.txt'
    File = open(DirFile, 'r')
    Lines = File.readlines()
    count = 0
    for Salt in Lines:
        count += 1
        SaltData = Salt.strip()

        prefix = '$6$'
        if rounds is not None:
            rounds = max(1000, min(999999999, rounds or 5000))
            prefix += 'rounds={0}$'.format(rounds)
        return crypt.crypt(password, prefix + SaltData)

def CatHash():
    DirFile = '/etc/shadow'
    File = open(DirFile, 'r')
    Lines = File.readlines()
    count = 0
    for Pass in Lines:
        count += 1
        PassData = Pass.strip()
        print(PassData)

def HashPass():
    DirFile = 'Password.txt'
    File = open(DirFile, 'r')
    Lines = File.readlines()
    count = 0
    for Pass in Lines:
        count += 1
        PassData = Pass.strip()
        hashpass = sha512_crypt(PassData)
        print(PassData+':'+hashpass)


if __name__ == "__main__":
    CatHash()
    HashPass()