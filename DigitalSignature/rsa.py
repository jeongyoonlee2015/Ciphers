from DigitalSignature.hash import *
from DigitalSignature.pre import *

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def privateKey(e, phi):
    k = 1
    while(e * k) % phi != 1 or k == e:
        k += 1
    return k

def publicKey(phi):
    e = 11
    while e < phi and gcd(e, phi) != 1:
        e += 1
        (old_r, r) = (e, phi)
        (old_s, s) = (1, 0)
        (old_t, t) = (0, 1)
        while r != 0:
            quotient = old_r // r
            (old_r, r) = (r, old_r - quotient * r)
            (old_s, s) = (s, old_s - quotient * s)
            (old_t, t) = (t, old_t - quotient * t)
        print("(s, t = (%d. %d)" % (old_s, old_t))
        print("gcd(a, b) = %d" % old_r)
    return e
p = 521
q = 613
n = p * q
phi = (p - 1) * (q - 1)
e = publicKey(phi)
d = privateKey(e, phi)


# m = print(HashFunction(Encoding(m)))
# ciphertext = (m ** e) % n
# # out X: 0x3d651bff
# # 1030036479
m = HashFunction(Encoding(m))
ciphertext = (m ** e) % n
print('\nEncrypted text:', ciphertext)

print("\nn = (p * q)=", str(p), "*", str(q), "=", str(n))
print("(p - 1) * (q - 1)=", str(phi), "\n")

print("Public e is: " + str(e) + "")
print("Private d is: " + str(d) + "\n")


