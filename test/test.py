import crypt
import string
import datetime
import subprocess
from pathlib import Path
import pathlib

#==================================================================

def Today():
    day_scan = datetime.date.today().strftime('%Y-%m-%d')
    return day_scan

def TimeYesterday():
    #Check date today
    check_today = datetime.date.today()
    #Check date yesterday
    check_yesterday = check_today - datetime.timedelta(days=1)
    #Format date yesterday to string
    yesterday = check_yesterday.strftime('%Y-%m-%d')
    return yesterday

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
    
import datetime
import subprocess
from pathlib import Path
import pathlib

def TestToday():
    day_scan = datetime.date.today().strftime('%Y-%m-%d')
    return day_scan
def SaltUser():
    day_scan = TestToday()
    DirFile = "ScanUser-"+day_scan+".txt"
    File = open(DirFile, 'r')
    Lines = File.readlines()
    count = 0
    print("Read File")
    for Salt in Lines:
        count += 1
        print("Dem")
        with open('/etc/shadow') as file:
            print("Read File")
            for line in file:
                if Salt in line:
                    total_salt = line.split("$")[2]
                    wlog = open("Salt-"+day_scan+".txt","a+")
                    wlog.write(total_salt+"\n")
                    print("Ghi")
        # return wlog
SaltUser()

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


    
