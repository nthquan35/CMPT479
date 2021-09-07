import random
import subprocess
import sys
import os
import time

def decrypt(ciphertext):
    cipherBlockCount = int(len(ciphertext) /16)
    result = bytearray()
    yN_minus_one = 0
    for n in range(2,cipherBlockCount+1):
        if not yN_minus_one:
            cipherLast = ciphertext[-(n-1)*16:]
        else:
            cipherLast = yN_minus_one

        randomBlock = "aaaaaaaaaaaaaaa"
        blockByte = bytearray()
        blockByte.extend(randomBlock.encode("ASCII"))
        i = 0
        blockByte.append(i)
        blockByte += cipherLast
        f = open("blockByte", "wb")
        f.write(blockByte)
        f.close()

        valid = 0

        #Check padding oracle for i
        while True:
            cmd = 'python3 oracle.py blockByte'.split()
            valid = subprocess.check_output(cmd, shell=False)

            if valid == b'1\n':
                break
            i += 1
            blockByte[15] = i

            f = open("blockByte", "wb")
            f.write(blockByte)
            f.close()

        dic = {}
        for j in range(15):
            k = 0
            while True:
                cmd = 'python3 oracle.py blockByte'.split()
                valid = subprocess.check_output(cmd, shell=False)
                if valid == b'1\n':
                    break
                else:
                    blockByte[j] = k
                    f = open("blockByte", "wb")
                    f.write(blockByte)
                    f.close()
                    dic[1] = j
                    k += 1

        decryptxN = bytes()
        if not dic:
            decryptxN = i ^ 1
        else:
            decryptxN = i ^ (17-dic[1])

        yN_minus_one = ciphertext[-n*16:-(n-1)*16]
        lastByte = decryptxN ^ yN_minus_one[15]
        result.insert(0,lastByte)
        # print(lastByte)


        #Decrypt block
        decryptionList = bytearray()
        decryptionList.append(decryptxN)

        for a in range(14,-1,-1):
            i, j = 0,1
            for b in range(len(decryptionList)):
                blockByte[a+j] = decryptionList[b] ^ (17 - (a + 1))
                j += 1
            blockByte[a] = 0
            f = open("blockByte", "wb")
            f.write(blockByte)
            f.close()
            valid = 0
            while True:
                cmd = 'python3 oracle.py blockByte'.split()
                valid = subprocess.check_output(cmd, shell=False)
                if valid == b'1\n':
                    break
                i += 1
                blockByte[a] = i

                f = open("blockByte", "wb")
                f.write(blockByte)
                f.close()

            decryptxN = i ^ (17 - (a + 1))
            decryptionList.insert(0,decryptxN)
            lastByte = decryptxN ^ yN_minus_one[a]
            # print(lastByte)
            result.insert(0,lastByte)
    return result


if __name__ == '__main__':
    # start_time = time.time()
    f = open(sys.argv[1], "rb")
    ciphertext = f.read()
    f.close()

    result = decrypt(ciphertext)

    os.remove("blockByte")
    f = open("decryptResult", "wb")
    f.write(result)
    f.close()
    # print("--- %s seconds ---" % (time.time() - start_time))
