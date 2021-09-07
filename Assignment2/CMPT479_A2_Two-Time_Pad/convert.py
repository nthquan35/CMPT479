
from os import closerange


def xor(a, b):
    #input: two bytearrays
    #output: bytearray of their xor
    if len(a) > len(b):
        temp = a
        a = b
        b = temp
    s = []
    for i in range(0, len(a)):
        s.append(a[i] ^ b[i])
    for i in range(len(a), len(b)):
        s.append(b[i])
    return s

def s_to_ints(s):
    #convert string to integer list ("bytearray")
    b = []
    for i in range(0, len(s)):
        b.append(ord(s[i]))
    return b

def ints_to_s(s):
    #convert string to integer list ("bytearray")
    b = []
    for i in range(0, len(s)):
        b.append(chr(s[i]))
    return b

in_file = open("ctext0", "rb") 
data0 = in_file.read()
in_file = open("ctext1", "rb")
data1 = in_file.read()
xorText = bytearray()
for i in range(400):
    xorText.append(data0[i] ^ data1[i])
# print(xorText)
# data0 = data0[:40]
# data1 = data1[:40]
xorText = xor(data0, data1)
# print(xorText)
# print(ints_to_s(xorText))

string = "Lambda Legal, an LGBT civil rights organization, co-signed a letter with 26 other gay rights organizations opposing Barrett's nomination. The letter expressed doubts about her ability to separate faith from her rulings on LGBT matters. During her Senate hearing, Barrett was questioned about landmark LGBTQ legal precedents such as Obergefell v. Hodges, United States v. Windsor, and Lawrence v. Texas. She "
byteTestString = bytes(string, 'ascii')
print(byteTestString)
result = bytearray()
for i in range(400):
    result.append(xorText[i] ^ byteTestString[i])
print(result)
# result = xor(xorText, byteTestString)
# print(ints_to_s(result))

# test = ints_to_s(result)
# dic = dict()
# for i in test:
#     if i not in dic:
#         dic[i] = 1
#     else:
#         dic[i] += 1
# # print(dic)
# a = sorted(dic.items(), key=lambda x: x[1])
# print(a)

print()

in_file.close()

