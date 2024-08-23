result = []
T = int(input())

for _ in range(T):
    C = int(input())

    quarters = C // 25
    C %= 25

    dimes = C // 10
    C %= 10

    nickels = C // 5
    C %= 5

    pennies = C


    result.append([quarters, dimes, nickels, pennies])

for i in result:
    print(' '.join(map(str, i)))