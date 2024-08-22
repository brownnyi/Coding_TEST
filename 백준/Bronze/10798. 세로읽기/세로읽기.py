# 입력 받기
words = []
for _ in range(5):
    words.append(input().strip())

# 최대 길이 찾기
max_len = max(len(word) for word in words)

# 결과 저장
result = []

# 세로로 읽기
for i in range(max_len):
    for word in words:
        if i < len(word):
            result.append(word[i])

# 결과 출력
print(''.join(result))