def solution(board):
    n = len(board) # 보드의 크기를 n에 저장합니다.
    # 각 칸을 순회하면서 지뢰가 있는 위치를 찾습니다.
    for y, row in enumerate(board):
        for x, area in enumerate(row):
            
            # 현재 위치에 지뢰가 있으면,
            if area == 1: 
        # 지뢰 주변의 8방향을 검사합니다.
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:

                        ny = y + dy
                        nx = x + dx

# 검사한 위치가 보드 내에 있고 해당 칸이 지뢰가 아니라면 "X"로 표시합니다.
                        if 0 <= ny < n and 0 <= nx < n and board[ny][nx] != 1:
                            board[ny][nx] = "X"

# "X"와 1로 표시된 칸을 제외한 안전한 지역()의 개수를 계산합니다.
    safe_area_count = sum([area.count(0) for area in board])

    return safe_area_count