def solution(a, b, c, d):
    dice = [a, b, c, d]

    count = (a == b) + (a == c) + (a == d) + (b == c) + (b == d) + (c == d)
    
    if count == 6:
        return 1111 * a
    
    elif count == 3:
        if a == b == c:
            p, q = a, d
        elif a == b == d:
            p, q = a, c
        elif a == c == d:
            p, q = a, b
        else:
            p, q = b, a
        return (10 * p + q) ** 2
    
    elif count == 2:
        freq = {}
        for num in dice:
            freq[num] = freq.get(num, 0) + 1
        p, q = [key for key in freq if freq[key] == 2]
        return (p + q) * abs(p - q)
    
    elif count == 1:
        freq = {}
        for num in dice:
            freq[num] = freq.get(num, 0) + 1
        p = [key for key in freq if freq[key] == 2][0]
        q, r = [key for key in freq if freq[key] == 1]
        return q * r
    
    else:
        return min(dice)