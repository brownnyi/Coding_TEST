def solution(quiz):
    answer = []
    for i in quiz:
        n1, op1, n2, op2, res = i.split()
        if op1 == '+':
            if (int(n1) + int(n2) == int(res)) == True:
                answer.append('O')
            else:
                answer.append('X')
        else:
            if (int(n1) - int(n2) == int(res)) == True:
                answer.append('O')
            else:
                answer.append('X')
    
    return answer