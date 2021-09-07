import math
import sys

def hammingCode(input):
    byteString = bytes(input, "ascii")
    binary_bitstring = (''.join(["{:08b}".format(x) for x in byteString]))
    binary_array = list(binary_bitstring)
    bit_length = len(binary_array)
    numOfParity = math.floor(math.log2(bit_length + 1) + 1)

    for i in range(numOfParity):
        binary_array.insert(pow(2,i) -1,'0')
    bit_length = len(binary_array)
    
    parity = []
    for i in range(numOfParity):
        position = pow(2,i) - 1
        skip = pow(2,i)
        result = 0
        count = skip
        while position < bit_length:
            result = int(binary_array[position]) ^ int(result)
            position = position + 1
            count -= 1
            if count == 0:
                position += skip
                count = skip
        parity.append(str(result))
    ret = ''.join(parity)
    return ret

if __name__ == '__main__':
    input = sys.argv[1]
    # print(input)
    result = hammingCode(input)
    print(result)
# print(''.join(binary_array))