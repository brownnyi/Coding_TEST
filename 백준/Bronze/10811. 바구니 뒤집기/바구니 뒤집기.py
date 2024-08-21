N, M = map(int, input().split())
basket = [i for i in range(1, N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    basket = basket[:a-1] + basket[a-1:b][::-1] + basket[b:]

for p in basket:
    print(p, end = " ")