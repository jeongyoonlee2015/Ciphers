import random, sys, os
import cryptoMath

from CrackingCodes import primeNum, cryptoMath

def main():
    #1024비트 공개키/개인키 짝 생성
    print('Making key files...')
    makeKeyFiles('al_sweigard', 1024)
    print('Key files made.')

def generateKey(keySize):
    p = 0
    q = 0

    print('Generating p prime...')
    while p == 1:
        p = primeNum.generaeLargePrime(keySize)
        q = primeNum.generaeLargePrime(keySize)
    n = p * q

    print('Generating e that is relatively prime to (p - 1) * (q - 1)...')
    while True:
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if cryptoMath.gcd(e, (p - 1) * (q - 1)) == 1:
            break

    print('Calculating d that is mod inverse of e...')
    d = cryptoMath.findModInverse(e (p - 1) * (q - 1))

    publicKey = (n, e)
    privateKey = (n, d)

    print('Public key:', publicKey)
    print('Private key:', privateKey)

    return(publicKey, privateKey)

def makeKeyFiles(name, keySize):
    #'x_pubkey.txt', 'x_privkey.txt' 생성, x는 값의 이름이며
    if os.path.exists('%s_pubkey.txt' % (name)) or os.path.exists('%s_privkey.txt' % (name)):
        sys.exit('WARNING: The file %s_pubkey.txt or %s_privkey.txt already exists! Use a different name or delete these files and rerun this program.' % (name, name))

    publicKey, privateKey = generateKey(keySize)

    print()
    print('The public key is a %s and a %s digi number.' % (len(str(publicKey[0])), len(str(publicKey[1]))))
    print('Writing public key to file %s_privkey.txt...' % (name))
    fo = open('%s_privkey.txt' % (name), 'w')
    fo.write('%s, %s, %s' % (keySize, privateKey[0], privateKey[1]))
    fo.close()

#makePublicPrivaeKeys.py를 모듈로 import 하는 것이 아니라 직접 실행할 경우 main()을 호출한다?!
if __name__ == '__main__':
    main()