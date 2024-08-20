def check_quadrant(x, y):
    if x > 0 and y > 0:
        print(1)
    elif x < 0 and y > 0:
        print(2)
    elif x < 0 and y < 0:
        print(3)
    else:
        print(4)

x = int(input())
y = int(input())

check_quadrant(x, y)