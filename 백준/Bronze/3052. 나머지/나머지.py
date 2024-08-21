n_list = []
for _ in range(10):
    a = int(input())
    n_list.append(a % 42)

print(len(set(n_list)))