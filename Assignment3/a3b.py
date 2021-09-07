from a3a import *
import sys

def correctData(string, position, givenParity):
    byteString = bytes(string, "ascii")
    binary_bitstring = (''.join(["{:08b}".format(x) for x in byteString]))
    binary_array = list(binary_bitstring)
    # binary_array.insert(0, '0')
    for i in range(len(givenParity)):
        binary_array.insert(pow(2,i) -1, givenParity[i])
    if position > len(binary_array):
        return '' 
    if binary_array[position-1] == '1':
        binary_array[position-1] = '0'
    else:
        binary_array[position-1] = '1'
    # remove parity bits
    for i in range(len(givenParity)-1,-1, -1):
        binary_array.pop(pow(2,i)-1)
    # remove most significant bits
    timesRemoveBits = int(len(binary_array) / 8)
    for i in range(timesRemoveBits-1, -1, -1):
        binary_array.pop(8*i)
    joinedBinary = ''.join(binary_array)
    ret = ''
    for i in range(0,len(joinedBinary), 7):
        ret += chr(int(joinedBinary[i:i+7],2))
    return ret

if __name__ == '__main__':
    string = sys.argv[2]
    result = hammingCode(string)
    givenParity = sys.argv[1]
    # print(givenParity)
    # print(result)
    if result == givenParity:
        print(givenParity)
        print(string)
    else:
        if len(result) != len(givenParity):
            print('The message is completely different!')
        else:
            position = 0
            for i in range(len(result)):
                if result[i] != givenParity[i]:
                    position += pow(2,i)
            # print(position)
            stringifyPosition = str(math.log2(position))
            if stringifyPosition[-1] == '0' and stringifyPosition[-2] == '.':
                pos = int(math.log2(position))
                listGivenParity = list(givenParity)
                if givenParity[pos] == '0':
                    listGivenParity[pos] = '1'
                else:
                    listGivenParity[pos] = '0' 
                print(''.join(listGivenParity))
                print(string)
            else:
                ret = correctData(string, position, givenParity)
                if ret == '':
                    print('The message is vastly different!')
                else:
                    print(givenParity)
                    print(ret)
            # print(position)