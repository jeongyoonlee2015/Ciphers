import pyperclip

def main():
    myMessage = 'Common sense is not so common.'
    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)

    # ciphertext에 들어 있는 암호화 된 문자열을 "파이프"문자 |와 함께 출력하는데 암호화 된 문자열의 끝에 공백이 있는 경우 이를 식별할 수 있음
    print(ciphertext + '|')

    # ciphertext에 들어 있는 암호화 된 문자열을 클립보드에 복사한다.
    pyperclip.copy(ciphertext)

def encryptMessage(key, message):
    # ciphertext의 각 문자열은 격자상 하나의 열에서 온 것임
    ciphertext = [''] * key

    # ciphertext의 각 열을 순회
    for column in range(key):
        currentIndex = column
        # currentIndex가 message 길이를 넘을 때까지 계속 순회 함
        while currentIndex < len(message):
            # ciphertext리스트 중 현재 col의 문자열 끝에 message의 currentIndex의 문자를 넣음
            ciphertext[column] += message[currentIndex]
            # currentIndex를 이동
            currentIndex += key
    # ciphertext 리스트를 문자열 한 개로 변환하고 리턴
    return ''.join(ciphertext)

# transpositionEncrypt.py를 실행하면 main()이 실행됨

if __name__ == '__main__': # dunder-main-dunder
    main()