import sys
a=int(input())
sum_list=[]

for i in range(0,a):
    x, y=map(int,sys.stdin.readline().split())
    sum_list.append(x+y)
for i in range(0,a):
    print(sum_list[i])