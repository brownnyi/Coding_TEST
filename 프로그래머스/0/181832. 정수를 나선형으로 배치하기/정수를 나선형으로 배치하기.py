def solution(n):
    sprial = [[0] * n for _ in range(n)]
     
    dx = [1, 0, -1, 0] 
    dy = [0, 1, 0, -1]

    x, y = 0, 0

    direction = 0

    for i in range(1, (n*n)+1):

        sprial[y][x] = i
        

        nx = x + dx[direction]
        ny = y + dy[direction]

        if nx >= n or nx < 0 or ny >= n or ny < 0 or sprial[ny][nx] != 0:
            direction = (direction + 1) % 4
            
            nx = x + dx[direction]
            ny = y + dy[direction]

        x, y = nx, ny
    
    return sprial