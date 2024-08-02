def solution(babbling):
    babb = ['aya','ye','woo','ma']
    result = []
    
    for i in babbling:
        for j in babb:
            i = i.replace(j,'x')
        result.append(i.replace('x',''))
        
    return result.count('')