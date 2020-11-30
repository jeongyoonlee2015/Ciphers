# Cracking Codes with Python
[Reference](https://nostarch.com/crackingcodes)
1.
2.
3.
4. [Reverse Cipher]()
5. [The Caesar Cipher]()
6. [Hackin the caesar cipher with Brute-Force]()
    * Brute-Force
        * 가능한 모든 복호 키로 암호 해독을 시도하는 것
        * 카이사르 암호를 해킹할 수 있음<br>```메시지의 비밀을 지키는 것이 암호의 핵심이며, 카이사르 암호는 이런 정보를 찾기 매우 쉽다.```
        * Kerckhoff's rule: <br>```암호의 동작 원리를 누구나 알고 있고 대상자가 아닌 누군가의 암호문을 갖고 있어도 그 암호가 여전히 안전해야 함```
        * Claude Shannon ```적은 그 시스템을 알고 있다.```
    
7. [Encrypting with the Transposition Cipher]()
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
        * 왼쪽 상단부터 시작해 각 열을 내려가면서 문자를 쓴다. <br> 열의 가장 아래에 이르면 오른쪽의 다음 열로 이동한다. <br> 지운 상자는 건너뛴다. 이것이 ```암호문```이 된다.
