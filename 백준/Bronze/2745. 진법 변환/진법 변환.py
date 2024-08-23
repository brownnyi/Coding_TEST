alpha_dic = {}
for i in range(ord('A'), ord('Z') + 1):
    alpha_dic[chr(i)] = i - 55
    
B, N = input().split()
N = int(N)
result = 0

# 문자열의 각 자리에 대해 계산을 수행
for i in range(len(B)):
    char = B[-(i + 1)]  # 역순으로 접근
    if char.isdigit():  # 숫자인 경우
        value = int(char)
    else:  # 알파벳인 경우
        value = alpha_dic[char]
    result += value * (N ** i)
    
print(result)
