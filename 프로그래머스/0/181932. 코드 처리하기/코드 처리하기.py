def solution(code):
    res = ''
    mode = 0
    for i in range(len(code)):
        if code[i] == '1':
            mode = 1 - mode
        else:
            if (mode == 0 and i % 2 == 0) or (mode == 1 and i % 2 == 1):
                res += code[i]
    return res if res else "EMPTY"