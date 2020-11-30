import random, sys, CrackingCodes.transpositionDecrypt, CrackingCodes.transpositionEncrypt

def main():
    random.seed(42) # 시드값을 상수로 설정

    for i in range(20): # 20회 테스트
    # 테스트용 무작위 메시지 생성
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)

        # message 문자열을 뒤섞기 위해 리스트로 만듦
        message= list(message)
        random.shuffle(message)
        message = ''.join(message) # 리스트를 다시 문자열로

    print('Test #%s: "%s..."' % (i + 1, message[:50]))

    # 각 message에 대해 가능한 모든 키 값 확인
    for key in range(1, int(len(message) / 2)):
        encrypted = CrackingCodes.transpositionEncrypt.encryptMessage(key, message)
        decrypted = CrackingCodes.transpositionDecrypt.decryptMessage(key, encrypted)

        # 원 message가 복호화 된 message와 다르면 에러 메시지 출력 후 프로그램 탈출
        if message != decrypted:
            print('Mismatch with key %s and message %s.' % (key, message))
            print('Decrypted as: ' + decrypted)
            sys.exit()
    print('Transposition cipher test passed.')

if __name__ == '__main__':
    main()