def xor(str1, str2):
    result = []
    for i, j in zip(str1, str2):
        result.append(chr(ord(i) ^ ord(j))
    return ''.join(result) 
 
xor1 = xor("flag", "{}[?")
print(xor1)

flag = xor(xor1, "{}[?")
print(flag)
