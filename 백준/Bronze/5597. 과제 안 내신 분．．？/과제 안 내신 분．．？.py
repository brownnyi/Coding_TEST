student = [i for i in range(1,31)]

for _ in range(28):
    n = int(input())
    student.remove(n)

for x in student:
    print(x)