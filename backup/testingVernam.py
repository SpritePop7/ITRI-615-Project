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

    print(Newkey)




def main():
    #testShortenKey()
    key = "hey"
    message = "hey you how are you doin"
    #testShortenOrLengthenKey(key, message)
    shortenOrLengthenKey(key, message)

if __name__ == "__main__":
    main()