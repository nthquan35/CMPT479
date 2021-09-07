# string = "This is a super long message!!!!"
# string = "This is a super "
# print(len(string))
# result = bytes(string, 'ascii')
# result = b'Alice and Bob in'
result = b'This is a super long message!!!!'
# print(result)
f = open("plaintext", "wb")
f.write(result)
f.close()
