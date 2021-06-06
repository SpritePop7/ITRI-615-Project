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
                print(sortKey)
    #print(permOrder)
    return permOrder


    
#add when working (self, main_window, key, file_data, filename, extension)
def transpositionEncrypt(self, main_window, key, file_data, filename, extension):
    #plaintext = "We are discovered. flee at once"
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
    plaintext = plaintext.ljust((row*col), ' ')

    tempPlain = ""
    chunks, chunk_size = len(plaintext), col 
    tempPlain = [plaintext[i:i+chunk_size] for i in range(0, chunks, chunk_size)]
    print(tempPlain)
    df = pd.DataFrame(index=np.arange(row), columns=np.arange(col))
    for i in range(row):
        k = 0
        for j in range(col):
            #print(j)
            #print(int(len(tempPlain[j])-1))
            while k != int(len(tempPlain[i])):
                df[k][i] = tempPlain[i][k]
                k += 1
    print(df)

    #use the permutation generated to read the 2d array by the column indicated to generate the ciphertext
    #used pandas transpose function to swap col and rows
    df_t = df.T
    print(df_t)

    ciphertext = ""    
    for j in range(len(permOrder)):
        for i in range(row):
            temp = int(permOrder[j]) - 1 
            #print(temp)
            ciphertext += df_t[i][temp]
    print(ciphertext)
    print(len(ciphertext))
    return ciphertext


def transpositionDecrypt():
    

#def main():
#    key = "Zebras"
#    transpositionEncrypt(key)

#if __name__ == '__main__':
#    main()


