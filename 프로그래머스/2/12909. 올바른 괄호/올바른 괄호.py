# def solution(s):
#     while '()' in s:
#         s = s.replace('()','')
#     return len(s) == 0

def solution(s):
    stack = []
    for c in s:
        if c=='(':
            stack.append(c)
        elif not stack or stack.pop()!='(':
                return False
    return False if stack else True