n = int(input())
result = []
for _ in range(n):
    result.append(input())

for i in result:
    print(i[0] + i[-1])