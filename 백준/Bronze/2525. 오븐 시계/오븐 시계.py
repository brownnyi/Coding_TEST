def oven(h, m, t):
    if m + t >= 60:
        if h + (1 * ((m + t) // 60)) >= 24:
            print(f'{h + (1 * ((m + t) // 60)) - 24} {m + t - (60 * ((m + t) // 60))}')
        else:
            print(f'{h + (1 * ((m + t) // 60))} {m + t - (60 * ((m + t) // 60))}')
    else:
        print(f'{h} {m + t}')

h, m = input().split()
h = int(h)
m = int(m)
t = int(input())
oven(h, m ,t)