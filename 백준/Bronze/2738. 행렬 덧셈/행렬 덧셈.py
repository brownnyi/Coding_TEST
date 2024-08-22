N, M = map(int, input().split())
one = []
two = []

# 첫 번째 행렬 입력
for _ in range(N):  # N줄에 걸쳐서 행렬을 입력받음
    one.append(list(map(int, input().split())))

# 두 번째 행렬 입력
for _ in range(N):  # N줄에 걸쳐서 행렬을 입력받음
    two.append(list(map(int, input().split())))

# 두 행렬의 합을 계산하여 새로운 행렬에 저장
total_sum = []
for y in range(N):  # 행렬의 행에 대해 반복
    row_sum = []
    for x in range(M):  # 행렬의 열에 대해 반복
        row_sum.append(one[y][x] + two[y][x])
    total_sum.append(row_sum)

# 결과 행렬 출력
for row in total_sum:
    print(" ".join(map(str, row)))

