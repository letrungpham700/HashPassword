import crypt

# def sha512_crypt(password, salt=None, rounds=None):
#     # if salt is None:
#     salt = 'hrEEvwUBF9x6rzbC'

#     prefix = '$6$'
#     if rounds is not None:
#         rounds = max(1000, min(999999999, rounds or 5000))
#         prefix += 'rounds={0}$'.format(rounds)
#     return crypt.crypt(password, prefix + salt)
    
# def yes_crypt(password, salt, rounds=None):
    # if salt is None:
    # salt = 'DHb8G5deVnOaO2cu3Xn.b.'

    # prefix = '$y$j9T$'
    # if rounds is not None:
    #     rounds = max(1000, min(999999999, rounds or 5000))
    #     prefix += 'rounds={0}$'.format(rounds)
    # return crypt.crypt(password, prefix + salt)

def CheckHash(rounds=None):
    DirFile = 'Password.txt'
    File = open(DirFile, 'r')
    Lines = File.readlines()
    count = 0
    for Pass in Lines:
        count += 1
        PassData = Pass.strip()
        # hashpass = sha512_crypt(PassData)
        # hashyes = yes_crypt(PassData)
        # print("SHA512 - "+PassData+':'+hashpass)
        # print(hashyes)
        print("Read file pass")

        DirFileS = 'Salt.txt'
        FileS = open(DirFileS, 'r')
        LinesS = FileS.readlines()
        count = 0
        for Salt in LinesS:
            count += 1
            SaltData = Salt.strip()
            print("Read file alt")
            prefix = '$y$j9T$'
            if rounds is not None:
                rounds = max(1000, min(999999999, rounds or 5000))
                prefix += 'rounds={0}$'.format(rounds)
                hashyes = crypt.crypt(PassData, prefix + SaltData)
            print(hashyes)

if __name__ == "__main__":
    x = CheckHash()
    print("Yescrypt -",x)