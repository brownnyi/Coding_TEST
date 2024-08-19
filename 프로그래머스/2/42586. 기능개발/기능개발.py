def solution(p, s):
    answer = []
    days = []
    cnt = 0

    for i in range(len(p)):
        d = (100 - p[i]) // s[i]
        if (100 - p[i]) % s[i] != 0:
            d = d + 1
        days.append(d)
    
    f = days[0]
    for j in range(len(days)):
        if f >= days[j]:
            cnt += 1
        else:
            answer.append(cnt)
            f = days[j]
            cnt = 1
    answer.append(cnt)
    return answer