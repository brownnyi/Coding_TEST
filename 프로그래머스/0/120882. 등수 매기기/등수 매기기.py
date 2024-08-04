def solution(score):
    answer = []
    val = [(i[0] + i[1]) / 2 for i in score]
    s_val = sorted(val, reverse = True)
    for i in val:
        answer.append(s_val.index(i) + 1)
        
    return answer