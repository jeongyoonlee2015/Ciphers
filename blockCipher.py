# From my Professor
#암호문 블록 결과: 1013912413 => C=hex(1013912413) => c = 0x3C6F135D
def BlockCipherEncrypt(K, P):
    P = 0x12345678 #P = hex(305419896)
    K = 0xC58FA10B #P = hex(3314524427)
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
        T = (T&0xffffffff) ^ K
    return T