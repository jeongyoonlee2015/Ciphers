#효율적인 거듭제곱 계산
#a^k mod n 계산
def exp_mod(a, k, n):
    answer = 1
    while k != 0:
        if(k & 1) == 1:
            answer = (answer * a) % n
        k = k >> 1
        a = (a * a) % n
    print(answer)

#n이 소수 또는 RSA 합성수가 아닌 경우 일반적으로 적용 불가
