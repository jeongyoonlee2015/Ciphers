# Assignment 8


* AS6 RSA
* AS7 Hash
> M -> hash(M) -> RSA(hash(M)) = (s) -> (M,  s)

## Assignment6 내용
1. 소수 p = 521과 q = 613에 대해, 공개키 e = 11, n = pq로부터 개인키 d를 구하시오.
2. 평문 M1 = 150000의 암호문 C1을 구하시오.
3. 암호문 C2 = 272301의 평문 M2를 구하시오.
* 답
    * 소수 p = 521, q = 613
    * n = p * q = 521 * 613 = 319373
    * phi(n) = (p - 1) * (q - 1) = 520 * 612 = 318240
    * e = 1이면 확장 유클리드 알고리즘에 의해, d = 28931
* m1 = 150000
    * c1 <br>= 121488<br>= (m1 ** e) % n<br> = 121488 % 319373    
* c2 = 272301
    * m2 <br>= 62342<br>= (c2 ** d) % n<br> = 62342 % 319373
             
## Assignment7 내용
> 과제5의 32비트 블록 암호를 이용하여 해시 함수와 MAC을 만들어 본다.
1. 과제 5의 블록암호에 Davies-Meyer모드를 적용하여 해시함수 Y = H(X)를 만든다.<br>(임의의 크기 x에 대해 32비트값 Y를 출력해야 함)
2. 1의 해시함수를 이용하여 HMAC을 만든다.<br>(상수 c1 = 0xabcdeff, 상수 c2 = 0x12345678)
3. 문자열 "Twinkle twinkle little star How I wonder what you are Up above the world so high Like a diamond in the sky Twinkle twinkle little star How I wonder what you are"에 대한 해시값과 MAC값을 계산한다.<br>MAC의 키 값: 0xcf36e59a 

### Assignment5 내용
* 블록 길이: 32bit
* 키 길이: 32bit
* P = 평문 블록
* K = 비밀키
* 8라운드 이후 32bit X값이 <U><strong>암호문 블록</strong></U>이 된다.
* 입출력형식(in Python)
    ```.py
    P = 0x12345678 #평문 블록
    K = 0xC58FA10B #키
    C = BlockCipherEncrypt(K, P) #암호문 블록
    ```
  
  
-------
# AS8 결과
* 전자서명 구성
    * 과제6 RSA암호(p=521, q=613, e=11, d = 28931)
    * 과제7 해시함수(32비트 해시값)
* 전자서명 s = 0x26a2d

* 전자서명 생성과정
    * 메시지
    * 해시함수 
        * 32비트: ```0x3e649af1```
    * RSA 복호화 (d,n) = (28931, 319373)
    * 전자서명값: ```0x26a2d```
    
* 전자서명 검증
    * 메시지 -> 해시함수 -> ```32비트``` -> mod 319373 -> ```0x2fb08``` 
    * 전자서명값: ```0x26a2d``` -> RSA복호화(e,n) = (11, 319373) -> ```0x2fb08```
    
    ```.py
    PublicKey(e, n) = (11, 319373)
    Private Key d = 28931
    Hash Value of m : 0x3e649af1
    Signature: 0x26a2d
    Verification:   
        s -> h%n: 0x2fb08
        m -> h%n: 0x2fb08
        => (m, s) is valid!
    ```