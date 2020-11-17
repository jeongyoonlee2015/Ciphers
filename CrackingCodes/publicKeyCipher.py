import sys, math
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!?.'

def main():
    filename = 'encrypted_file.txt'#쓰거나 읽을 파일
    mode = 'encrypt' #encrypt or decrypt모드 설정
    if mode == 'encrypt':
        message = ''
        pubKeyFilename = 'al_sweigart_pubkey.txt'
        print('Encryping and writing to %s...' % (filename))
        encryptedext = encryptAndWriteToFile(filename, pubKeyFilename, message)

        print('Encrypted text:')
        print(encryptedext)

    elif mode == 'decrypt':
        privKeyFilename = 'al_sweigart_privkey.txt'
        decryptedText = readFromFileAndDecrypt(filename, privKeyFilename)

        print('Decrypted text:')
        print(decryptedText)

def getBlocksFromText(message, blockSize):
    for character in message:
        if character not in SYMBOLS:
            print('ERROR: The symbol set does not have the character %s' % (character))
            sys.exit()
    blockInts = []
    for blockStart in range(0, len(message), blockSize):
        blockInt = 0
        for i in range(blockStart, min(blockStart + blockSize, len(message))):
            blockInt += (SYMBOLS.index(message[i])) * (len(SYMBOLS) ** (i % blockSize))
        blockInts.append(blockInt)
    return blockInts

def getTextFromBlocks(blockInts, messageLength, blockSize):
    message = []
    for blockInt in blockInts:
        blockMessage = []
        for i in range(blockSize -1, -1, -1):
            if len(message) + i < messageLength:
                charIndex = blockInt // (len(SYMBOLS) ** i)
                blockInt = blockInt % (len(SYMBOLS) ** i)
                blockMessage.insert(0, SYMBOLS[charIndex])
        message.extend(blockMessage)
    return ''.join(message)

def encryptMessage(message, key, blockSize):
    #message문자열을 블록 정수 값의 리스트로 변환 -> 각 블록 정수 값을 암호화 한다. 암호화를 위해 공개 키를 받아야 함
    encryptedBlocks = []
    n, e = key

    for block in getBlocksFromText(message, blockSize):
        #ciphertext = plaintext ^ e mod n
        encryptedBlocks.append(pow(block, e, n))
    return encryptedBlocks

def decryptMessage(encryptedBlocks, messageLength, key, blockSize):
    #암호화된 블록 정수 값들의 리스트를 원문 message 문자열로 복호화
    #원문 message 길이는 마지막 블록까지 완전히 복호화되기 위해 필요
    #복호화를 위해 개인 키를 받아야 함
    decryptedBlocks = []
    n, d = key
    for block in encryptedBlocks:
    #plaintext = ciphertext ^ e mod n
        decryptedBlocks.append(pow(block, d, n))
    return getTextFromBlocks(decryptedBlocks, messageLength, blockSize)

def readKeyFile(keyFilename):
    fo = open(keyFilename)
    content = fo.read()
    keySize, n, EorD = content.split(',')
    return(int(keySize), int(n), int(EorD))

def encryptAndWriteToFile(messageFilename, keyFilename, message, blockSize = None):
    # 키파일의 키를 이용해 message를 암호화하고 파일로 저장함
    # 암호화 된 message 문자열을 리턴함
    keySize, n, e = readKeyFile(keyFilename)
    if blockSize == None:
        #blockSize를 지정하지 않으면 키 크기와 심볼 집합 크기가 허용하는 가장 큰 값을 블록 크기로 정함
        blockSize = int(math.log(2 ** keySize, len(SYMBOLS)))
    if not(math.log(2 ** keySize, len(SYMBOLS)) >= blockSize):
        sys.exit('ERROR: Block size is too large for the key and symbol set size. Did you specify the correct key file and encrypted file?')
    encryptedBlocks = encryptMessage(message, (n, e), blockSize)

    for i in range(len(encryptedBlocks)):
        encryptedBlocks[i] = str(encryptedBlocks[i])
        encryptedContent = ','.join(encryptedBlocks)

    encryptedContent = '%s_%s_%s' % (len(message), blockSize, encryptedContent)
    fo = open(messageFilename, 'w')
    fo.write(encryptedContent)
    fo.close()

    return encryptedContent

def readFromFileAndDecrypt(messageFilename, keyFilename):
    #키파일을이용해 파일로부터 암호화된 메시지를 읽고 복호화
    keySize, n, d = readKeyFile(keyFilename)

    fo = open(messageFilename)
    content = fo.read()
    messageLength, blockSize, encryptedMessage = content.split('_')
    messageLength = int(messageLength)
    blockSize = int(blockSize)

    if not(math.log(2 ** keySize, len(SYMBOLS)) >= blockSize):
        sys.exit('ERROR: Block size is too large for the key and symbol set size. \n Did you specify the correct key file and encrypted file?')

    encryptedBlocks = []
    for block in encryptedMessage.split(','):
        encryptedBlocks.append(int(block))

    return decryptMessage(encryptedBlocks, messageLength, (n, d), blockSize)

if __name__ == '__main__':
    main()
