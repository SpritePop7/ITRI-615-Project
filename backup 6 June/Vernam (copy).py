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
    print(len(Newkey))
    print(len(message))
    
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

def BinaryToDecimal(binary):    
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return (decimal)

def asciiToBina(text):
    res = ''.join(format(ord(i), '08b') for i in text)
    #print(res)
    return(res)

def vernam1(self,main_window, key, file_data,filename,extension):
    key = shortenOrLengthenKey(key, file_data)
    file_data = asciiToBina(file_data)
    print(key)
    key = asciiToBina(key)
    result = int(file_data,2) ^ int(key,2)
    result = bin(result)[2:].zfill(len(file_data))
    
    #convert to ascii
    result = int(result, 2)
    print(result)
    byte_number = result.bit_length() + 7 // 8
    binary_array = result.to_bytes(byte_number, "big")
    result = binary_array.decode()

    print(result)
    #return result

def vernam2(self,main_window, key, file_data, filename,extension):
    file_source = main_window.plainTextEdit_5.toPlainText()
    f = open(file_source, 'r')
    filedata = f.read()
    print(type(filedata))
    binFileData = asciiToBina(filedata)
    newKey = shortenOrLengthenKey(key, filedata)
    print(newKey)
    binKey = asciiToBina(newKey)
    binResult = int(binFileData,2) ^ int(binKey,2)
    binResult = bin(binResult)[2:].zfill(len(binFileData))
    print(binResult)
    
    #result = int(binResult,2) ^ int(binKey,2)
    #result = bin(result)[2:].zfill(len(binFileData))
    
    #convert to ascii
    binResult = int(binResult, 2)
    byte_number = binResult.bit_length() + 7 // 8
    binary_array = binResult.to_bytes(byte_number, "big")
    result = binary_array.decode()
    print(result)
    f = open(filename + "Vernam" + extension , 'w')
    f.write(result)
    f.close()

def vernamEnc(self,main_window,key, file_data,filename,extension):
    #get message length to save for decryption
    messagelength = "/"
    messagelength += str(len(file_data))
    print(messagelength)
    #get plaintext and convert to binary
    binMessage = asciiToBina(file_data)
    print(binMessage)
    #generate key and convert to binary
    key = shortenOrLengthenKey(key, file_data)
    print(key)
    binKey = asciiToBina(key)
    print(binKey)
    #produce ciphertext by xor key and plaintext 
    xorResult = int(binMessage,2) ^ int(binKey,2)
    binResult = bin(xorResult)[2:].zfill(len(binMessage))
    print(len(binResult))
    str_data = ''
    for i in range(0, len(binResult),7):
        temp_data = int(binResult[i:i+7])
        decimal_data = BinaryToDecimal(temp_data)
        str_data = str_data + chr(decimal_data)
    str_data += messagelength
    print(str_data)
    f = open(filename + "Vernam" + extension , 'w')
    f.write(str_data)
    f.close()

def vernamDecr(self,main_window,key,file_data,filename,extension):
    
