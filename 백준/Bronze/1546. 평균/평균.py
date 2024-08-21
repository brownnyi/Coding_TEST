N = int(input())
cnt = 0
scores = list(map(int,input().split()))

M = max(scores)

for i in range(len(scores)):
   scores[i] = scores[i]/M*100
   cnt += scores[i]

print(cnt/len(scores))