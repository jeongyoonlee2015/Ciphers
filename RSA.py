#2nd RSA Code

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

mode = input("encrypt or decrypt?: ")
if mode == 'encrypt':
    # m1 = 150000
    m1 = int(input('암호화 할 텍스트를 입력하세요.:'))
    ciphertext = (m1 ** e) % n
    print('\nEncrypted text:', ciphertext)
elif mode == 'decrypt':
    # c2 = 272301
    c2 = int(input('복호화 할 텍스트를 입력하세요.:'))
    plaintext = (c2 ** d) % n
    print('\nDecrypted text:', plaintext)

print("\nn = (p * q)=", str(p), "*", str(q), "=", str(n))
print("(p - 1) * (q - 1)=", str(phi), "\n")

print("Public e is: " + str(e) + "")
print("Private d is: " + str(d) + "\n")



# #init RSA Code
#
# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
#
# def privateKey(e, phi):
#     k = 1
#     while(e * k) % phi != 1 or k == e:
#         k += 1
#     return k
#
# def publicKey(phi):
#     e = 11
#     while e < phi and gcd(e, phi) != 1:
#         e += 1
#         (old_r, r) = (e, phi)
#         (old_s, s) = (1, 0)
#         (old_t, t) = (0, 1)
#         while r != 0:
#             quotient = old_r // r
#             (old_r, r) = (r, old_r - quotient * r)
#             (old_s, s) = (s, old_s - quotient * s)
#             (old_t, t) = (t, old_t - quotient * t)
#         print("(s, t = (%d. %d)" % (old_s, old_t))
#         print("gcd(a, b) = %d" % old_r)
#     return e
# p = 521
# q = 613
# n = p * q
# phi = (p - 1) * (q - 1)
#
# # def encryption(m, e):
# #     n = 319373
# #     ciphertext = (m ** e) % n
# #     return ciphertext
#
# def decryption(c, d):
#     n = 319373
#     plaintext = (c ** d) % n
#     return plaintext
#
# mode = input("type a word encrypt or decrypt")
#
# e = publicKey(phi)
# d = privateKey(e, phi)
#
# if mode == 'encrypt':
#     m = input("텍스틀를 입력해주세요.")
#     ciphertext = (m ** e % n)
#     print('Encrypted text:')
#     # print(encryption)
#
# elif mode == 'decrypt':
#     c = input("텍스틀를 입력해주세요.")
#     print('Decrypted text:')
#     print(decryption)
#
# ciphertext = (m ** e % n)
# print("\n")
# print("n = (p * q)=", str(p), "*", str(q), "=", str(n))
# print("(p - 1) * (q - 1)=", str(phi))
# print("\n")
# print("Public e is: " + str(e) + "")
# print("Private d is: " + str(d) + "")
# print("\n")
# print('Encrypted text:', ciphertext)