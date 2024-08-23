N, B = map(int, input().split())

result = ""
while N > 0:
    remainder = N % B
    if remainder >= 10:
        result += chr(remainder + 55)  # 10 이상의 경우 알파벳으로 변환
    else:
        result += str(remainder)  # 10 미만의 경우 숫자로 변환
    N //= B

# 결과는 역순으로 구해지므로 뒤집어서 출력
print(result[::-1])
