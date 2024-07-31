def solution1(binomial):
    return eval(binomial)

def solution(binomial):
    a,op,b = binomial.split()

    a,b = int(a), int(b)
    
    if op == '+':
        return a + b

    elif op == '-':
        return a - b

    else:
        return a*b