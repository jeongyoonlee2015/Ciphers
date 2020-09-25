# RC4
* RC4 (Rivest Cipher 4 also known as ARC4 or ARCFOUR meaning Alleged RC4, see below) is a stream cipher. <br> It has been used for WPA and WPA2.
* The RC4 was created to be symmetric, the encryption phase is identical to decryption.

# Structure of RC4 Cipher
1. Key Scheduling (1byte <= key length <= 256byte)

```
// Pseudocode
for i = 0 ... 255 {
 t[i] = i
}
j = 0
k = length(cle)
for i = 0 ... 255 {
 j = (j + t[i] + key[i % k]) % 256
 swap t[i] <-> t[j]
}
```

2. Pseudo - Random Generator

```
 // Pseudocode
 a = b = 0
 j = length(string)
 codes = []
 for i = 0 ... j {
  a = (a + 1) % 256
  b = (b + t[a]) % 256
  swap t[a] <-> t[b]
  codes []= ( t[ (t[a] + t[b]) % 256] ) XOR string[i]
 }
 print codes
 ```
