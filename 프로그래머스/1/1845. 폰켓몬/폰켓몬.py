def solution(nums):
    pick = len(nums) / 2
    p = set(nums)
    
    if len(p) >= pick:
        return pick
    else:
        return len(p)