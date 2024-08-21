alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]

word = input()
n_list = []

for a in alphabet:
    if a in word:
        n_list.append(str(word.index(a)))
    else:
        n_list.append('-1')

print(' '.join(n_list))