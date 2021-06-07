
def vigenereEncrypt(self, main_window, key, file_data, filename, extension):
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
    #Displaying the ciphertext and write to file
    main_window.plainTextEdit_Cipher.setPlainText(encryptedText)
    vigfile = filename + extension
    f = open(vigfile, 'w')
    f.write(encryptedText)
    f.close()
    return encryptedText


def vigenereDecrypt(self, main_window, key ,file_data, filename, extension):
    #Creating the variables for decryption
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.()?’!/\n "
    letterIndex = dict(zip(alphabet, range(len(alphabet))))
    IndexLetter = dict(zip(range(len(alphabet)), alphabet))
    decryptedText = ''
    
    #making the message and key the same size before encrypting
    split_cipher = [file_data[i:i+len(key)] for i in range(0, len(file_data), len(key))]
    #converting the message to an index and adding the key
    for splitEach in split_cipher:
        i = 0
        for letter in splitEach:
            number = (letterIndex[letter] - letterIndex[key[i]]) % len(alphabet)
            decryptedText += IndexLetter[number]
            i+=1
    #Displaying the plaintext and write to file
    main_window.plainTextEdit_Cipher.setPlainText(decryptedText)
    vigfile = filename + extension
    f = open(vigfile, 'w')
    f.write(decryptedText)
    f.close()
    return decryptedText