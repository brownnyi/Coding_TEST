num_matrix = []
max_matrix = []

for _ in range(9):
    matrix = list(map(int, input().split()))
    num_matrix.append(matrix)
    max_matrix.extend(matrix)

max_num = max(max_matrix)

for y in range(9):
    for x in range(9):
        if num_matrix[y][x] == max_num:
            print(max_num)
            print(y + 1, x + 1)