# Cracking Codes with Python
[Reference](https://nostarch.com/crackingcodes)
1. [Making paper Cryptography tools]()<br>
2. [Programmin in the interactive shell]()<br> 
3. [Strings and Writing programs]()<br>
4. [Reverse Cipher]()<br>
5. [The Caesar Cipher]()<br>
6. [Hackin the caesar cipher with Brute-Force]()<br>
    * Brute-Force
        * 가능한 모든 복호 키로 암호 해독을 시도하는 것
        * 카이사르 암호를 해킹할 수 있음<br>```메시지의 비밀을 지키는 것이 암호의 핵심이며, 카이사르 암호는 이런 정보를 찾기 매우 쉽다.```
        * Kerckhoff's rule: <br>```암호의 동작 원리를 누구나 알고 있고 대상자가 아닌 누군가의 암호문을 갖고 있어도 그 암호가 여전히 안전해야 함```
        * Claude Shannon ```적은 그 시스템을 알고 있다.```
    <br>
7. [Encrypting with the Transposition Cipher]()<br>
    * Caesar Cipher의 한계: 컴퓨터로 66개의 가능한 모든 키를 무차별 대입법으로 공격하는 것은 어려운 일이 아니기 때문
    * Transposition Cipher의 특성
        * 가능한 키의 수가 메시지의 길이에 좌우되므로 무차별 대입법으로 깨기 더 어려움
        * 문자를 다른 문자로 바꾸지 않고 메시지 심볼을 재정렬해 원래 메시지를 읽을 수 없게 만드는 기법
        * 각 키는 문자의 순서를 바꾸거나 뒤섞기 때문에 암호 분석가는 암호문을 원래 메시지로 다시 배열하는 방법을 알 수 없음
        
    * Types of Transposition Cipher: ```전치암호``` / ```분할된 전치암호```
        * [rail fence]()
        * [route]()
        * [가로장]()
        * [경로]()
        * [Myszkowski]()
    * Process of Encryption
        * 메시지와 키의 문자 수를 센다.
        * 키와 같은 개수의 상자를 한 줄에 그린다. <br>(eg: 키가 8개면 상자도 8개)
        * 왼쪽에서 오른쪽으로 상자를 채우고 상자 한 개에 글자 한 개를 넣는다.
        * 문자가 상자 끝에 이르면 상자의 줄을 한 줄 더 그린다.
        * 마지막 문자까지 오면 마지막 행에 있는 사용하지 않은 상자는 칠해둔다.
        * 왼쪽 상단부터 시작해 각 열을 내려가면서 문자를 쓴다. <br> 열의 가장 아래에 이르면 오른쪽의 다음 열로 이동한다. <br> 지운 상자는 건너뛴다. 이것이 ```암호문```이 된다. <br>
  
8. [Decrypting with the Transposition Cipher]()
    <br>
    * Process of Decryption
        * 메시지 길이를 키로 나누고 반올림해 필요한 열 수를 계산
        * 상자를 열과 행으로 그린다. 앞에서 계산한 마큼 열을, 키 값만큼 행을 그린다.
        * 상자의 총 개수(행과 열의 길이를 곱한 값)에서 암호문의 길이를 빼서 검게 칠할 상자 수를 계산
        * 가장 오른쪽 아래 칸에 3단계에서 계산한 값만큼 칠한다.
        * 가장 윗줄에서부터 왼쪽에서 오른족으로 한칸씩 암호문의 문자를 넣는다. 검게 칠한 상자는 건너뛴다.
        * 가장 왼쪽 열에서부터 위에서 아래로 읽고 이 과정을 모든 열에서 수행해 평문을 얻는다.
        <br>
        
9. [Programming a program to test your program]()<br>
    * 8,9에서 만든 전치 암호화 프로그램은 암복호화에 효과적인 것으로 보이지만 항상 제대로 동작하는지 알 수 없음
    * 암호화 프로그램을 테스트하는 프로그램을 9장에서 작성해 본다.
    * ```transpositionEncrpyt.py```에서 ```decryptMessage()```에 암호문 전달 <br> -> ```decryptMessage()```에 의해 리턴된 평문이 원문과 같으면 암복호화 프로그램이 잘 동작한다고 판단할 수 있
    <br>

10. [Encrypting and Decrypting Files]()<br>
    * 수백만 글자에 달하는 파일 전체를 암호화/복호화하기
    <br>

11. [Detecting english programmatically]()<br>

    <br>

12. [Hacking the Transposition cipher]()<br>

    <br>

13. [A Modular Arithmetic module for the Affine Cipher]()<br>
    * 곱셈암호
        * 카이사르 암호와 비슷하지만 더하기가 아닌 곱하기로 암호화를 수행
        * 아핀 암호는 곱셈암호와 카이사르 암호를 결합해 더 강력하고 안전한 암호화를 구현
        * 나머지 연산 & 최대공약수 이용 [cryptomath.py]()
    <br>

14. [Programming the Affine Cipher]()<br>
    * 아핀 암호는 암호화 과정에서 서로 다른 암호 두 개를 사용하기 때문에 키도 두 개가 필요한 암호
        * 곱셈 암호용
        * 카이사르 암호용
        * 정수 한 개를 키 두 개로 분할해보
        
    * 아핀 암호는 몇 개의 키를 보유할 수 있는가?
        * 아핀 암호의 키 B는 심볼 집합의 크기만큼으로 제한됨
        * 키 A는 심볼 집합 크기와 서로소 관계이기만 하면 얼마든지 커도 될 것 같다고 생각할 수 있다. 하지만 카이사르 암호는 심볼 집합을 순회하므로 큰 암호 키와 작은 암호 키의 결과가 같은 결과가 같은 경우가 존재한다는 점을 지닌다.
    ```.py
    # affineKeyTest.py
    # 아핀 암호의 키 공간이 len(SYMBOLS) ^ 2미만인 것을 검증
    from CrackingCodes import affineCipher, cryptoMath

    message ='Make thins as simple as possible, but not simpler.'

    for keyA in range(2, 80):
        key = keyA * len(affineCipher.SYMBOLS) + 1
        if cryptoMath.gcd(keyA, len(affineCipher.SYMBOLS)) == 1:
            print(keyA, affineCipher.encryptMessage(key,message))
    ```
    <br>

15. [Hacking the Affine Cipher]()<br>
    <br>

16. []()<br>

    <br>

17. []()<br>

    <br>

18. []()<br>
    <br>

19. []()<br>


    <br>

20. []()<br>

    <br>

21. []()<br>

    <br>

22. []()<br>
    <br>

23. []()<br>

    <br>

    <br>

24. []()<br>

    <br>
