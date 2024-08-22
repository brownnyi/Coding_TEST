chess = [1,1,2,2,2,8]
white = list(map(int, input().split()))
result = []
for i in range(len(white)):
    result.append(chess[i] - white[i])

for r in result:
    print(r, end = ' ')