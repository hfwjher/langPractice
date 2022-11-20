"""
一个可以将韩语unicode编码转化成hex的函数
题目想法来源为：
sunshinectf2022_Crypto_Exotic Bytes
"""
def unicodeKrToHex(x:str):
    result = ""
    for i in x:
        result += chr(int("0x"+str(hex(ord(i)))[-2:],16))
    return result
a = "걳걵걮걻걢갴걳갳걟갱갲갸걟갱갵걟걢갱건걟걲갳걭갴거거갱걮걧걽"
print(unicodeKrToHex(a))