# 그룹 단어인지 확인하는 함수
def is_group_word(word):
    seen_letters = []
    last_char = ''
    
    for char in word:
        if char != last_char:  # 이전 문자와 다른 경우에만 실행
            if char in seen_letters:  # 이전에 본 문자지만 연속적이지 않은 경우
                return False
            seen_letters.append(char)
        last_char = char
    
    return True

# 입력 받기
N = int(input())
count = 0

# N개의 단어 입력 받아 그룹 단어 개수 계산
for _ in range(N):
    word = input().strip()
    if is_group_word(word):
        count += 1

# 결과 출력
print(count)