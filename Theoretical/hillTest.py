import numpy as np
from sympy import Matrix
import string
import random
dim = 2
alphabet = string.ascii_uppercase
key = np.matrix([[1, 2], [2, 5]])

def main():
    mode = input("Select Encrypt or Decrypt:")
    if mode == 'Encrypt' or 'encrypt':
        encrypt()
    elif mode == 'Decrypt' or 'decrypt':
        decrypt()

def encrypt():
    plaintext = input("Input your plaintext for encryption:")
    encryption = ""
    for index, i in enumerate(plaintext):
        values = []
        if index % dim == 0:
            for j in range(dim):
                if (index + j < len(plaintext)):
                    values.append([alphabet.index(plaintext[index + j])])
                else:
                    values.append([random.randint(0, 25)])

            vector = np.matrix(values)
            vector = key * vector
            vector %= 26
            for j in range(dim):
                encryption += alphabet[vector.item(j)]
    print(encryption)

def decrypt():
    ciphertext = input("Input your ciphertext for decryption:")
    decryption = ""
    key = Matrix(np.matrix([[1, 2], [2, 5]]))
    key = key.inv_mod(26)
    key = key.tolist()

    for index, i in enumerate(ciphertext):
        values = []

        if index % dim == 0:
            for j in range(dim):
                values.append([alphabet.index(ciphertext[index + j])])

            vector = np.matrix(values)
            vector = key * vector
            vector %= 26

            for j in range(dim):
                decryption += alphabet[vector.item(j)]
    print(decryption)

if __name__ == '__main__':
    main()