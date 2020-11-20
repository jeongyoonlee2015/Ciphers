from HashMAC import *
m = "Twinkle twinkle little star How I wonder what you are Up above the world so high Like a diamond in the sky Twinkle twinkle little star How I wonder what you are"
M0 = Encoding(m)
P = 0x12345678  # P = hex(305419896)
K = 0xC58FA10B  # K = hex(3314524427)
T = BlockCipherEncrypt(K, P)

print("T:", hex(T))
print("Encoding m is:\n", M0)
print(hex(HashFunction(M0)))