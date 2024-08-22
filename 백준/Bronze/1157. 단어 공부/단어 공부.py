n = input()
n = n.lower()
n_list = list(set(n))
result = []

for i in n_list:
    result.append(n.count(i))

if result.count(max(result)) > 1:
    print('?')
else:
    print(n_list[result.index(max(result))].upper())