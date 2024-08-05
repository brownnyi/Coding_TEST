def solution(sides):
    side = sides[:]
    count  = 0
    
    for i in range(1, sum(sides)):
        side = sides[:]
        side.append(i)
        side = sorted(side)
        
        if side[-1] < sum(side[:-1]):
            count += 1
            
    return count