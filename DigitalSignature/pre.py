from DigitalSignature.blockCipher import BlockCipherEncrypt
m = "Twinkle twinkle little star How I wonder what you are Up above the world so high Like a diamond in the sky Twinkle twinkle little star How I wonder what you are"
def Encoding(m):#문자열 인코딩
    M = []
    for i in range(len(m)):#문자열 길이만큼 돌리기
        M.append(ord(m[i]))
    return M#최종적으로 만들어진 배열 반환
#X = 0xa5c8f1ee

#압축함수구현: Davies-Meyer
# x = 0xa5c8f1ee  # x = hex(2781409774)
def CompressionFunction(x, m):#둘다 32bit m: 메시지 블록
    y = BlockCipherEncrypt(m, x) ^ x #키, 평문 블록
    return y