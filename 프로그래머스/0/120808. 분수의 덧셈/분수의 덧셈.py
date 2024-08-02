def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solution(numer1, denom1, numer2, denom2):
    # 분수의 덧셈
    numerator = numer1 * denom2 + numer2 * denom1
    denominator = denom1 * denom2
    
    # GCD 계산
    g = gcd(numerator, denominator)
    
    # 기약 분수로 만들기
    reduced_numerator = numerator // g
    reduced_denominator = denominator // g
    
    return [reduced_numerator, reduced_denominator]