# 아핀 암호의 키 공간이 len(SYMBOLS) ^ 2미만인 것을 검증
from CrackingCodes import affineCipher, cryptoMath

message ='Make thins as simple as possible, but not simpler.'

for keyA in range(2, 80):
    key = keyA * len(affineCipher.SYMBOLS) + 1
    if cryptoMath.gcd(keyA, len(affineCipher.SYMBOLS)) == 1:
        print(keyA, affineCipher.encryptMessage(key,message))