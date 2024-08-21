N, M = map(int,input().split())

N_list = [0] * N
# N_list의 각 요소의 위치 : N_list[N-1]

for q in range(M):
    i, j, k = map(int, input().split())
    for w in range(i, j+1):
        N_list[w-1] = k

for e in range(N):
    print(N_list[e], end = ' ')