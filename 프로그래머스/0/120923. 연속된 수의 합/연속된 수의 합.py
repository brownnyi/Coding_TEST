def solution(num, total):
    n = 0
    for i in range(-1000 , total + 1):
        if (num * i) + sum(j for j in range(num)) == total:
            n = i

    return [n + e for e in range(num)]