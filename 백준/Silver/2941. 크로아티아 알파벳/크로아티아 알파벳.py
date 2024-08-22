croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()

for c in croatia:
    s = s.replace(c, ' A ')

s_list = list(s.split())
cnt = 0
for i in s_list:
    if len(i) >= 2 and i not in croatia:
        cnt += len(i)
    else:
        cnt += 1
print(cnt)