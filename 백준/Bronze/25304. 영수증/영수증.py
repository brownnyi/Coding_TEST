x = int(input())
n = int(input())
total_price = 0

for _ in range(n):
    price, num = map(int, input().split())
    total_price += (price * num)
    
if total_price == x:
    print('Yes')
else:
    print('No')