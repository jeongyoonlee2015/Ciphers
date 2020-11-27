import numpy as np
from sympy import Matrix
import string
import random
dim = 2 #n차원 행렬
cipher = string.ascii_uppercase
def main():
    mode = input("Select Encrypt or Decrypt:")
    if mode == 'Encrypt':
        encrypt()
    elif mode == 'Decrypt':
        decrypt()

def encrypt():
    key = np.matrix([[1, 2], [2, 5]])
    plaintext = input("Input your plaintext for encryption:")
    encryption = ""
    for index, i in enumerate(plaintext):
        value = []
        if index % dim == 0:
            for j in range(0, dim):
                if (index + j < len(plaintext)):
                    value.append([cipher.index(plaintext[index + j])])
                else:
                    value.append([random.randint(0, 25)])

            vector = np.matrix(value)
            vector = key * vector
            vector %= 26
            for j in range(0, dim):
                encryption += cipher[vector.item(j)]
    print(encryption)

def decrypt():
    ciphertext = input("Input your ciphertext for decryption:")
    decryption = ""
    key = np.matrix([[1, 2], [2, 5]])
    key = Matrix(key)
    key = key.inv_mod(26)
    key = key.tolist()

    for index, i in enumerate(ciphertext):
        value = []

        if index % dim == 0:
            for j in range(0, dim):
                value.append([cipher.index(ciphertext[index + j])])

            vector = np.matrix(value)
            vector = key * vector
            vector %= 26

            for j in range(0, dim):
                decryption += cipher[vector.item(j)]
    print(decryption)

if __name__ == '__main__':
    main()