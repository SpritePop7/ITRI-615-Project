import pandas as pd
import math
import numpy as np

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

def reverseString(string):
    return string[::-1]

    
#A function for encrypting a file using the transposition algorithm
def transpositionEncrypt(self, main_window, key, file_data, filename, extension):
    #get the col length from the key
    plaintext = file_data
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
    #df = df.fillna('')
    #print(df)
    #use the permutation generated to read the 2d array by the column indicated to generate the ciphertext
    #used pandas transpose function to swap col and rows to use the same for loops above to get the ciphertext
    #df_t = df.T
    #print(df_t)

    ciphertext = ""    
    for j in range(len(permOrder)):
        for i in range(row):
            temp = int(permOrder[j]) - 1 
            #print(temp)
            ciphertext += df[temp][i]
    print(ciphertext)
    print(len(ciphertext))
    main_window.plainTextEdit_Cipher.setPlainText(ciphertext)
    f = open(filename + extension , 'w')
    f.write(ciphertext)
    f.close()
    return ciphertext

#A function for dencrypting a file using the transposition algorithm

def transpositionDecrypt(self, main_window, key, file_data, filename, extension):
    #f = open("PlainText.txt", 'r')
    #file_data = f.read()
    #print(file_data)    
    rows = int(len(file_data) / len(key))
    print(rows)
    tempPlain = ""
    chunks, chunk_size = len(file_data), rows 
    tempPlain = [file_data[i:i+chunk_size] for i in range(0, chunks, chunk_size)]
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
    print(plaintext)
    main_window.plainTextEdit_Cipher.setPlainText(plaintext)
    f = open(filename + extension , 'w')
    f.write(plaintext)
    f.close()
    return plaintext
