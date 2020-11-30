import pyperclip

message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM' # 암복호화할 문자열
key = 13

mode = input('encrypt of decrypt: ')

SYMBOLS= 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
translated = ''

for symbol in message:

    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]

    else:
        # 암복호화하지 않은 문자를 더함
        translated = translated + symbol

print(translated)
pyperclip.copy(translated)

