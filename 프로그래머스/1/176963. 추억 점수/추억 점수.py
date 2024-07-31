def solution(name, yearning, photo):
    answer = []
    score = {name[i]:yearning[i] for i in range(len(name))}
    for i in photo:
        s = 0
        for j in i:
            if j in score:
                s += score[j]
            else:
                s += 0
        answer.append(s)
            
    return answer