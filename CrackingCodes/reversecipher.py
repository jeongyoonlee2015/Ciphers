#https://www.nostarch.com/crackingcodes(BSD Licensed)
#message = 'Hallo Ich bin Joy'
message = input ('enter message:')
translated = ''

i = len(message) - 1 #변수 i에 값을 저장하는 할당문
while i >= 0:
    translated = translated + message[i]
    i = i - 1 #그 다음 문자

print(translated)