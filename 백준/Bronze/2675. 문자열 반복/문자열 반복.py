result = []
T = int(input())

for _ in range(T):
    word = ''
    n, s = input().split()
    for i in s:
        word += i * int(n)
    result.append(word)

for w in result:
    print(w)