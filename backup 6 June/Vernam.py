import math, binascii
from os import read

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

def getKeyValue(filename, extension , key):
    f = open(filename + extension, 'r')
    data = f.read()
    splitData = data.partition("/")
    print(splitData)
    return splitData

def decryptionKey(key, value):
    number = int(value) / len(key)
    number = math.floor(number)
    NewKey = ""
    for i in range(number):
        NewKey += key
    if len(NewKey) > int(value):
        NewKey = NewKey[0:int(value)]
    if len(NewKey) < int(value):
        NewKey = NewKey.ljust(int(value), 'k')
    print(NewKey)
    return NewKey




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

def vernamEnc(self,main_window,key, file_data,filename,extension):
    #get message length to save for decryption
    messagelength = ""
    messagelength += str(len(file_data)) + "/"
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
    str_data = messagelength + str(binResult)
    print(str_data)
    #Display encrypted data and write to file
    main_window.plainTextEdit_Cipher.setPlainText(str_data)
    f = open(filename + extension , 'w')
    f.write(str_data)
    f.close()
    return str_data
    
def vernamDecr(self,main_window,key,file_data,filename,extension):
    #generate key from value infront of ciphertext
    splitdata = getKeyValue(filename,extension,key)
    NewKey = decryptionKey(key, splitdata[0])
    print(NewKey)
    binKey = asciiToBina(NewKey)
    print(binKey)
    #get ciphertext from getKeyValue return 
    binMessage = splitdata[2]
    #produce plaintext by xor key and ciphertext 
    xorResult = int(binMessage,2) ^ int(binKey,2)
    binResult = bin(xorResult)[2:].zfill(len(binMessage))
    print(binResult)    
    binResult = int(binResult, 2)
    byte_number = binResult.bit_length() + 7 // 8
    binary_array = binResult.to_bytes(byte_number, "big")
    result = binary_array.decode()
    result = result[-int(splitdata[0]):]
    print(result)
    #Display plaintext and write to file
    main_window.plainTextEdit_Cipher.setPlainText(result)
    f = open(filename + extension , 'w')
    f.write(result)
    f.close()
    return result


