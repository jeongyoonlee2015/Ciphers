import numpy as np
from sympy import Matrix
import string
import random
dim = 2
alphabet = string.ascii_uppercase
key = np.matrix([[1, 2], [2, 5]])

def main():
    mode = input("Select Encrypt or Decrypt:")
    if mode == 'Encrypt':
        enHill()
    elif mode == 'Decrypt':
        deHill()

def enHill():
    message = 'HAPPYNEWYEAR'
    encryption = ""

    for index, i in enumerate(message):
        values = []
        if index % dim == 0:
            for j in range(0, dim):
                if (index + j < len(message)):
                    values.append([alphabet.index(message[index + j])])
                else:
                    values.append([random.randint(0, 25)])

            vector = np.matrix(values)
            vector = key * vector
            vector %= 26
            for j in range(0, dim):
                encryption += alphabet[vector.item(j)]
    print(encryption)

def deHill():
    message = 'HOTBYJWOGQIH'
    decryption = ""
    key = np.matrix([[1, 2], [2, 5]])
    key = Matrix(key)
    key = key.inv_mod(26)
    key = key.tolist()

    for index, i in enumerate(message):
        values = []

        if index % dim == 0:
            for j in range(0, dim):
                values.append([alphabet.index(message[index + j])])

            vector = np.matrix(values)
            vector = key * vector
            vector %= 26

            for j in range(0, dim):
                decryption += alphabet[vector.item(j)]
    print(decryption)

if __name__ == '__main__':
    main()