def find_fraction(n):
    diagonal = 1  # 대각선 번호
    count = 0  # 현재까지 몇 개의 분수를 세었는지
    
    # 대각선이 어디에 있는지 찾기
    while count < n:
        count += diagonal
        diagonal += 1
    
    diagonal -= 1
    count -= diagonal
    
    # 대각선 내에서의 인덱스
    index_in_diagonal = n - count
    
    # 대각선이 짝수인지 홀수인지에 따라 분수 계산
    if diagonal % 2 == 0:
        # 짝수 대각선: 분자가 줄고 분모가 증가
        numerator = index_in_diagonal
        denominator = diagonal - index_in_diagonal + 1
    else:
        # 홀수 대각선: 분자가 증가하고 분모가 줄어듦
        numerator = diagonal - index_in_diagonal + 1
        denominator = index_in_diagonal
    
    print(f'{numerator}/{denominator}')
    
n = int(input())
find_fraction(n)