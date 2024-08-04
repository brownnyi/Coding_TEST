def solution(polynomial):
    answer = ''
    a = polynomial.split(" + ")
    b, c = [], []
    for i in a:
        if i.isdigit():
            c.append(i)
        else:
            b.append(i)
    d, e = 0, 0

    for i in b:
        d += 1 if i.isalpha() else int(i[:-1])
    for i in c:
        e += int(i)
    if d and e:
        answer = f'x + {e}' if d == 1 else f'{d}x + {e}'
    elif d and not e:
        answer = f'x' if d == 1 else f'{d}x'
    elif not d and e:
        answer = f'{e}'

    return answer