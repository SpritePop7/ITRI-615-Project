import binascii
import math


def testShortenKey():
    message = "hello"
    key = "hello you how are you doing"
    print(key)
    key = key[0: len(message)]

    print(key)

def testShortenOrLengthenKey(key, message):
    print(message)
    if len(key) > len(message):
        key = key[0:len(message)]

    if len(key) < len(message):
        #number = len(message) - len(key)
        key = key.ljust(len(message), 'k')
    #print(number)
    print(key)
    print(len(key))
    print(len(message))

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

    return(Newkey)


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

def asciiToBina(text):
    res = ''.join(format(ord(i), '08b') for i in text)
    #print(res)
    return(res)

def main():
    f = open("PlainTextVernam.txt", 'r')
    data = f.read()
    print(data)


def main1():
    #testShortenKey()
    key = "hey"
    message = "hey you how are you doin"
    binKey = ''
    binMessage = ''
    newKey = ""
    #testShortenOrLengthenKey(key, message)
    #shortenOrLengthenKey(key, message)
    test = "Hey how are you"
    #test = binascii.hexlify(test)
    print(test)
    #print(hexaToBin(test))
    newKey = shortenOrLengthenKey(key, message)
    #newKey = str(newKey)
    
    print(newKey)
    binKey = asciiToBina(newKey)
    binMessage = asciiToBina(message)
    print(binKey)
    print(binMessage)
    result = int(binMessage,2) ^ int(binKey,2)
    result = bin(result)[2:].zfill(len(binMessage))
    print(result)
    result = int(result,2) ^ int(binKey,2)
    result = bin(result)[2:].zfill(len(binMessage))
    print(result)

    result = int(result, 2)
    byte_number = result.bit_length() + 7 // 8
    binary_array = result.to_bytes(byte_number, "big")
    result = binary_array.decode()
    print(result)


if __name__ == "__main__":
    main()