from decrypt import *
import sys
import random
# import subprocess

def encrypt(plaintext):
    lenPlaintext = len(plaintext)
    if lenPlaintext % 16 != 0:
        print("The plaintext size is not multiple of 16!")
        return
    
    lastEncryptedBlock = ""
    for _ in range(16):
        lastEncryptedBlock += chr(random.randint(97,122))
    # iv = b'CMPT 479 test iv'
    blockByte = bytearray(lastEncryptedBlock, 'utf-8')
    # test = plaintext + blockByte 

    result = bytearray()
    result += blockByte
    plaintextBlockCount = int(lenPlaintext / 16)
    for i in range(plaintextBlockCount):
        if i == 0:
            text = plaintext[-16:] + blockByte
            nextEncryptBlock = decrypt(text)
            result = nextEncryptBlock + result
        else:
            text = plaintext[-16*(i+1):-16*i] + result[0:16]
            nextEncryptBlock = decrypt(text)
            result = nextEncryptBlock + result
    return result
    

if __name__ == '__main__':
    f = open(sys.argv[1], "rb")
    plaintext = f.read()
    f.close()
    # print(plaintext)
    result = encrypt(plaintext)

    f = open("encryptResult", "wb")
    f.write(result)
    f.close()