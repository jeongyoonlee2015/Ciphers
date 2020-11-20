m = "Twinkle twinkle little star How I wonder what you are Up above the world so high Like a diamond in the sky Twinkle twinkle little star How I wonder what you are"
def Encoding(m):#문자열 인코딩

    M = []
    for i in range(len(m)):
        M.append(ord(m[i]))
    return M

#X = 0xa5c8f1ee

def BlockCipherEncrypt(K, P):# 키, 평문블록
    P = 0x12345678  # P = hex(305419896)
    K = 0xC58FA10B  # K = hex(3314524427)
    S = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7]
    T = K ^ P
    X = [0 for j in range(8)]
    Y = [0 for j in range(8)]
    Z = [0 for j in range(8)]

    for i in range(8):
        for j in range(8): X[j] = (T >> (4 * j)) & 0xf
        for j in range(8): Y[j] = S[X[j]]

        Z[0] = Y[0] ^ Y[2] ^ Y[3] ^ Y[5] ^ Y[6] ^ Y[7]
        Z[1] = Y[0] ^ Y[1] ^ Y[3] ^ Y[4] ^ Y[6] ^ Y[7]
        Z[2] = Y[0] ^ Y[1] ^ Y[2] ^ Y[4] ^ Y[5] ^ Y[7]
        Z[3] = Y[1] ^ Y[2] ^ Y[3] ^ Y[4] ^ Y[5] ^ Y[6]
        Z[4] = Y[0] ^ Y[1] ^ Y[5] ^ Y[6] ^ Y[7]
        Z[5] = Y[1] ^ Y[2] ^ Y[4] ^ Y[6] ^ Y[7]
        Z[6] = Y[2] ^ Y[3] ^ Y[4] ^ Y[5] ^ Y[7]
        Z[7] = Y[0] ^ Y[3] ^ Y[4] ^ Y[5] ^ Y[6]

        for j in range(8): T = (T << 4)| Z[7 - j]
        T = (T & 0xffffffff) ^ K
    return T

#압축함수구현: Davies-Meyer
# x = 0xa5c8f1ee  # x = hex(2781409774)

def CompressionFunction(X, M):#둘다 32bit
    M1 = BlockCipherEncrypt(X, M) ^ M
    return M1

#해시함수
def HashFunction(M):
    #MD-Strengthening Padding
    Mblock = []#메시지 블록 배열
    Mlen = len(M) #메시지 길이(바이트 수) = 16비트 값
    Mblen = 0#메시지 블록

    if Mlen % 4 == 0:
        for i in range(Mlen // 4):
            temp = (M[4 * i] << 24) | (M[4 * i + 1] << 16) | (M[4 * i + 2] << 8) | M[4 * i + 3]
            Mblock.append(temp)
        temp = (0x80000000) | Mlen
        Mblock.append(temp)

    elif Mlen % 4 == 1:
        for i in range (Mlen // 4):
            temp = (M[4 * i] << 24) | (M[4 * i + 1] << 16) | (M[4 * i + 2] << 8) | M[4 * i + 3]
            Mblock.append(temp)
        temp = (M[Mlen - 1] << 24) | (0x800000) | Mlen
        Mblock.append(temp)

    elif Mlen % 4 == 2:
        for i in range (Mlen // 4):
            temp = (M[4 * i] << 24) | (M[4 * i + 1] << 16) | (M[4 * i + 2] << 8) | M[4 * i + 3]
            Mblock.append(temp)
        temp = (M[Mlen - 2] << 24) | (M[Mlen - 1] << 16) | (0x8000)
        Mblock.append(temp)
        Mblock.append(Mlen)

    else: #Mlen % 4 == 3:
        for i in range (Mlen // 4):
            temp = (M[4 * i] << 24) | (M[4 * i + 1] << 16) | (M[4 * i + 2] << 8) | M[4 * i + 3]
            Mblock.append(temp)
        temp = (M[Mlen - 3] << 24) | (M[Mlen - 2] << 16) | (M[Mlen - 1] << 8) | (0x80)
        Mblock.append(temp)
        Mblock.append(Mlen)

    # X = 0xa5c8f1ee

    X = 0xa5c8f1ee
    Y = CompressionFunction(X, Mblock[i])
    j = i + 1
    for j in range(Mblen):
        Y = CompressionFunction(Y, Mblock[j])
        return Y
    print("out Y:", Y)
    return Y

# from testAS7 import *
# M = Encoding(m)
# print(hex(HashFunction(M)))
# out Y: 470704440
# 0x1c0e6138