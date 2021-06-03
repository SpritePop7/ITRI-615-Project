import math, binascii
from os import read

def hexaToBin(hex):
    try:
        ans = bin(int(hex,16))[2:]
        while (len(ans)%(4*len(hex)) != 0):
            ans = "0" + ans
        return ans
    except (ValueError, TypeError) as error:
            print("hexToBin:")
            print(error)



def deciToBin(num):
    try:
        b = bin(num)[2:]
        while (len(b)%4 != 0):
            b = "0" + b
            return b
    except (ValueError, TypeError) as error:
            print("decToBin:")
            print(error)

def binaToHex(bi):
    try:
        return '%0*X' % ((len(bi) + 3) // 4, int(bi, 2))
    except (ValueError, TypeError) as Error:
        print("binToHex:")
        print(Error)

def deciToHex(n):
    try:
        return binaToHex(deciToHex(n))
    except (ValueError, TypeError) as Error:
        print("decToHex:")
        print(Error)

def xor(i, p):
    try:
        ans = ""
        while (len(i) != len (p)):
            if (len(i) < len(p)):
                i = "0" + i
            elif (len(i) > len(p)):
                p = "0" + p
        ans = deciToHex(int(i,16)^int(p,16))
        while(len(ans) != len(i)):
            ans = "0" + ans
        return ans
    except (ValueError, TypeError) as error:
        print("xor:")
        print(error)
   

def shortenOrLengthenKey(key, message):
    number = len(message) / len(key)
    number = math.floor(number)
    Newkey = ""
    for i in range(number):
        Newkey += key
        
    if len(Newkey) > len(message):
        Newkey = Newkey[0:len(message)]

    if len(Newkey) < len(message):
        #number = len(message) - len(key)
        Newkey = Newkey.ljust(len(message), 'k')
    print(Newkey)
    return Newkey

    

def vernamEncrypt(self, main_window, key, file_data, filename, extension):
    file_source = main_window.plainTextEdit_5.toPlainText()
    f = open(file_source, 'rb')
    filedata = f.read()
    f.close()
    print(filedata)
    plainTextBinary = binascii.hexlify(filedata)
    print(plainTextBinary)
    plainTextBinary = hexaToBin(filedata)
    Newkey = shortenOrLengthenKey(key, filedata)
    Newkey = Newkey.encode(encoding='utf-8')
    Newkey = binascii.hexlify(Newkey)
    print(Newkey)
    Newkey = hexaToBin(Newkey)
    cipherText = xor(hexaToBin(plainTextBinary),hexaToBin(Newkey))
    print(cipherText)
    #f = open(filename + "Encrypted" + extension)
    #f.write(cipherText)
    #f.close()