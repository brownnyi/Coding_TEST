#실패코드
def solution(board, h, w):
    n = len(board)
    count = 0

    dh = [0,1,-1,0]
    dw = [1,0,0,-1]

    for i in range(len(board[0])):  #len(board[0]) 쓸수 없는 이유 4*4가 아닌 5*5와 같이 다르게 나올 수도 있기 때문에 dh[4]와 같은 경우 찾을 수가 없음
        h_check = h + dh[i]
        w_check = w + dw[i]

        if (0 <= h_check < n) and (0 <= w_check < n):
            if board[h][w] == board[h_check][w_check]:
                count += 1

    return count

#개선코드
def solution(board, h, w):
    n = len(board)
    count = 0

    dh = [0,1,-1,0]
    dw = [1,0,0,-1]

    for i in range(dh)):
        h_check = h + dh[i]
        w_check = w + dw[i]

        if (0 <= h_check < n) and (0 <= w_check < n):
            if board[h][w] == board[h_check][w_check]:
                count += 1

    return count
