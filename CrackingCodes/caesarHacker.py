message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
SYMBOLS= 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# 가능한 모듴 키를 순회
for key in range(len(SYMBOLS)):

    # translated에 공백 문자열을 넣어서 이전 순회의 translated 값을 비우는 것이 중요함
    translated = ''
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

        if translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)
            # 복호화 된 심볼을 더함
            translated = translated + SYMBOLS[translatedIndex]

        else:
            translated = translated + symbol # 암복호화 없이 심볼을 더함

    print('Key #%s: %s' % (key, translated))

# 카이사르 암호의 최대취약점: 암호화할 때 쓸 수 있는 키가 많지 않다는 것
# 메시지의 보안 수준을 더 높이려면 더 많은 키가 있어야 함
# 전치 암호를 통해 보안성을 높일 수 있음