from Crypto.Cipher import AES
import sys


key = b'you saw nothing!'
iv = b'CMPT 479 test iv'
f = open(sys.argv[1], "rb")
ciphertext = f.read()
f.close()

cipher = AES.new(key, AES.MODE_CBC, iv)
# print(cipher)
plaintext = cipher.decrypt(ciphertext)
# print(plaintext)
#last byte must be padding
padnum = plaintext[-1]
if padnum == 0:
    print("0")
    sys.exit(0)
passed_check = True
for i in range(2, padnum+1):
    if plaintext[-i] != padnum:
        passed_check = False
        break
if passed_check == True:
    print("1")
else:
    print("0")

# print(ciphertext)

