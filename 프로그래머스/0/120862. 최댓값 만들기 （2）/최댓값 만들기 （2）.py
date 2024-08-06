def solution(numbers):
    return max([j * y for i,j in enumerate(numbers) for x, y in enumerate(numbers) if i != x])