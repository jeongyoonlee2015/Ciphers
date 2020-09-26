import binascii

message = 'plainplain'
key = 'plain form password'

# Key Scheduling
S = list(range(256))
j = 0

for i in range(256):
    j = (i + S[i] + ord(key[i % len(key)])) % 256
    S[i], S[j] = S[j], S[i]

# Random Generator
i = 0
j = 0
stream_code = []
for i in range(len(message)):
    i = (i + 1) % 256
    j = (j + S[i]) % 256

    S[i], S[j] = S[j], S[i]
    calc = (S[(S[i] + S[j]) % 256])
    stream = S[calc]
    stream_code.append(stream)

# Print Result (난관봉착)

    def convert_key(s):
        return [ord(c) for c in s]
    key = convert_key(key)

    keystream = S(key)

    print(keystream, binascii.format(keystream))# print(stream, '{:08b}'.format(stream))
