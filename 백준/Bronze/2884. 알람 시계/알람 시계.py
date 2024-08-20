def alarm(h, m):
    if m < 45:
        if h - 1 < 0:
            print(f'23 {m + 60 - 45}')
        else:
            print(f'{h - 1} {m + 60 - 45}')
    else:
        print(f'{h} {m - 45}')

h, m = input().split()
h = int(h)
m = int(m)

alarm(h, m)