def dice_check(f, s, t):
    dice_list = [int(f), int(s), int(t)]
    unique_dice = set(dice_list)
    
    if len(unique_dice) == 1:  # 같은 눈이 3개인 경우
        return 10000 + (dice_list[0] * 1000)
    elif len(unique_dice) == 2:  # 같은 눈이 2개만 있는 경우
        for i in unique_dice:
            if dice_list.count(i) == 2:
                return 1000 + (i * 100)
    else:  # 모두 다른 눈이 나오는 경우
        return max(dice_list) * 100

f, s, t = input().split()

result = dice_check(f, s, t)
print(result)