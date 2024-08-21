word_list = []
while True:
    try:
        word = input().strip()  # 입력받은 문자열에서 앞뒤 공백 제거
        if word == "":  # 빈 문자열일 경우 반복문 종료
            break
        word_list.append(word)
    except:
        break

for i in word_list:
    print(i)