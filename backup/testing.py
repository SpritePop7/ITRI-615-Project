import binascii, os

def binToHex(bi):
    try:
        return '%0*X' % ((len(bi) + 3) // 4, int(bi, 2))
    except (ValueError, TypeError) as Error:
        print("binToHex:")
        print(Error)

def hexToBin(hex):
    try:
        ans = bin(int(hex,16))[2:]
        while (len(ans)%(4*len(hex)) != 0):
            ans = "0" + ans
        return ans
    except (ValueError, TypeError) as error:
        print("hexToBin:")
        print(error)

#with open("index.png", "rb") as f:
    #byte = f.readlines()
    #print(byte[3])
    #while byte != EOFError:
        #Do stuff with byte.
        #byte += f.read(1)
        #print(byte)

file = open("index.png", "rb")
name, extension = os.path.splitext(file)
print(name)
print(extension)

byte = file.read()
file.close()
#print(byte)
imagehex = binascii.hexlify(byte)
#print(imagehex)
imagebin = hexToBin(imagehex)
#print(imagebin)
imagehex2 = binToHex(imagebin)
byte2 = binascii.unhexlify(imagehex2)

f = open("demo.png", "wb")
f.write(byte2)
f.close()





#while byte:
 #   imagedata = binascii.hexlify(byte)
  #  print(imagedata)
    #imagedata += binToDec(byte)
    


