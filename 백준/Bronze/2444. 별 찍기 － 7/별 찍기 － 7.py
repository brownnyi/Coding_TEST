N = int(input())

for i in range(1, 2 * N):
    if i <= N:
        star = '*' * (2 * i - 1)
        print(' ' * (N - i) + star)
    else:
        star = '*' * (2 * (2 * N - i) - 1)
        print(' ' * (i - N) + star)