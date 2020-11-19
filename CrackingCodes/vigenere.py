#비즈네르, 다중 문자 치환 암호
import pyperclip

LETTERS = 'ABCDEFGHIJKLMNOPQRSUTVWXYZ'

def main():
    myMessage ="""Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist."""
    myKey = 'ASIMOV'
    myMode = 'encrypt'#Select encrypt || decrypt

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)

    print('%sed message:' % (myMode.title()))
    print(translated)
    pyperclip.copy(translated)
    print()
    print('The message has been copied to the clipboard.')


def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')

def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')

def translateMessage(key, message, mode):
    translated = [] #암복호화된 메시지 문자열 저장
    keyIndex = 0
    key = key.upper()

    for symbol in message: #메시지 각 심볼 순회
        num = LETTERS.find(symbol.upper())
        if num != -1: # -1은 sybol.upper()가 LETTERS에 존재하지 않는다는 의미
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex])
            elif mode =='decrypt':
                num -= LETTERS.find(key[keyIndex])

            num %= len(LETTERS) #LETTER길이를 초과할 경우 한 바퀴 돌린다?!

            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0

        else:
            translated.append(symbol)

    return ''.join(translated)

if __name__ =='__main__':
    main()
