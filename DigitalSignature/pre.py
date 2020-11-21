from DigitalSignature.blockCipher import BlockCipherEncrypt
m = "Twinkle twinkle little star How I wonder what you are Up above the world so high Like a diamond in the sky Twinkle twinkle little star How I wonder what you are"
def Encoding(m):#문자열 인코딩

    M = []
    for i in range(len(m)):
        M.append(ord(m[i]))
    return M
#X = 0xa5c8f1ee

#압축함수구현: Davies-Meyer
# x = 0xa5c8f1ee  # x = hex(2781409774)

def CompressionFunction(X, M):#둘다 32bit
    M1 = BlockCipherEncrypt(X, M) ^ M
    return M1