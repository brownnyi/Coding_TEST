a, x = map(int, input().split())
n_list = input().split()
result = []
for i in n_list:
    if int(i) < x:
        result.append(i)

print(' '.join(result))