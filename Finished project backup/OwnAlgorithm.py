import math
import numpy as np
import pandas as pd

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

#A function for getting the length of the plaintext so that it can be added to the ciphertext for decryption at a later stage
def getKeyValue(filename, extension , key):
    f = open(filename + extension, 'r')
    data = f.read()
    splitData = data.partition("/")
    print(splitData)
    return splitData

#A function that takes the key and the value that was produced in the getKeyValue function in order to recreate the key for correct decryption
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

#A function to convert a Binary string to a Decimal string
def BinaryToDecimal(binary):    
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return (decimal)

#A function that takes a ascii string and converts it to a binary string
def asciiToBina(text):
    res = ''.join(format(ord(i), '08b') for i in text)
    #print(res)
    return(res)

def findPermOrder(key):
    permOrder = ""
    keyCheck = key.lower()
    keyLength = len(key)
    sortKey = sorted(keyCheck)
    #print(sortKey)
    #print(keyLength)
    for i in range(keyLength):
        for j in range(keyLength):
            if(keyCheck[i] == sortKey[j]):
                permOrder += str(j+1)
                #sortKey = sortKey[j:len(sortKey)]
                #print(sortKey)
    #print(permOrder)
    return permOrder

def ownAlgorithmEnc(self, main_window, key, file_data, filename, extension):
    #Creating the variables for the encryption
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.()?’!/\n "
    letterIndex = dict(zip(alphabet, range(len(alphabet))))
    IndexLetter = dict(zip(range(len(alphabet)), alphabet))
    encryptedText = ''

    #making the message and key the same size before encrypting
    split_message = [file_data[i:i+len(key)] for i in range(0, len(file_data), len(key))]
    #converting the message to an index and adding the key
    for splitEach in split_message:
        i = 0
        for letter in splitEach:
            number = (letterIndex[letter] + letterIndex[key[i]]) % len(alphabet)
            encryptedText += IndexLetter[number]
            i+=1
    plaintext = encryptedText
    keyLength = len(key)
    #get the permutation from the key
    permOrder = findPermOrder(key)
    print(permOrder)

    #add the plaintext into the 2d array by the amount of the row length
    col = keyLength
    row = len(plaintext) / keyLength 
    row = math.ceil(row)
    #filling the string with spaces to the size of the array
    plaintext = plaintext.ljust((row*col), ' ')
    tempPlain = ""
    chunks, chunk_size = len(plaintext), col 
    tempPlain = [plaintext[i:i+chunk_size] for i in range(0, chunks, chunk_size)]
    print(tempPlain)
    df = pd.DataFrame(index=np.arange(row), columns=np.arange(col))
    for i in range(row):
        k = 0
        for j in range(col):
            while k != int(len(tempPlain[i])):
                df[k][i] = tempPlain[i][k]
                k += 1
    print(df)
    
    ciphertext = ""    
    for j in range(len(permOrder)):
        for i in range(row):
            temp = int(permOrder[j]) - 1 
            #print(temp)
            ciphertext += df[temp][i]
    print(ciphertext)
    print(len(ciphertext))
    
    messagelength = ""
    messagelength += str(len(ciphertext)) + "/"
    print(messagelength)
    #get plaintext and convert to binary
    binMessage = asciiToBina(ciphertext)
    print(binMessage)
    #generate key and convert to binary
    key = shortenOrLengthenKey(key, ciphertext)
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

def ownAlgorithmDec(self, main_window, key, file_data, filename, extension):
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

    rows = int(len(result) / len(key))
    print(rows)
    tempPlain = ""
    chunks, chunk_size = len(result), rows 
    tempPlain = [result[i:i+chunk_size] for i in range(0, chunks, chunk_size)]
    print(tempPlain)
    df = pd.DataFrame(index=np.arange(rows), columns=np.arange(len(key)))
    for i in range(len(key)):
        k = 0
        for j in range(rows):
            while k != int(len(tempPlain[i])):
                df[i][k] = tempPlain[i][k]
                k += 1
    print(df)
    keyValue = findPermOrder(key)
    print(keyValue)

    df2 = pd.DataFrame(index=np.arange(rows), columns=np.arange(len(key)))
    k = 0
    #print(df[5][4])
    for i in range(len(key)):
        for j in range(rows): 
            df2[i][j] = df[int(keyValue[k])-1][j]
        k += 1
    #print(df2)
    plaintext = ""
    for i in range(rows):
        for j in range(len(key)):
            plaintext += df2[j][i]
    
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.()?’!/\n "
    letterIndex = dict(zip(alphabet, range(len(alphabet))))
    IndexLetter = dict(zip(range(len(alphabet)), alphabet))
    decryptedText = ''
    
    #making the message and key the same size before encrypting
    split_cipher = [plaintext[i:i+len(key)] for i in range(0, len(plaintext), len(key))]
    #converting the message to an index and adding the key
    for splitEach in split_cipher:
        i = 0
        for letter in splitEach:
            number = (letterIndex[letter] - letterIndex[key[i]]) % len(alphabet)
            decryptedText += IndexLetter[number]
            i+=1
    main_window.plainTextEdit_Cipher.setPlainText(decryptedText)
    f = open(filename + extension , 'w')
    f.write(decryptedText)
    f.close()
    return decryptedText
