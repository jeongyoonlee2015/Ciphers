def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def findModInverse(a, m):
    # a * x % m = 1을 만족하는 a와 m의 모듈러 역수를 리턴
    if gcd(a, m) != 1:
        return None #a와m이 서로소 관계가 아니면 모듈러 역수가 없음

    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m