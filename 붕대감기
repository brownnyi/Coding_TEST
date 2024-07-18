def solution(bandage, health, attacks):
    heal_time = 0 #heal_time을 통해 공격을 받았을 때나, t와 같아졌을때 활용하기 위해
    hp = health
    t, x, y = bandage

#어택 타임, 공격 데미지 구하기
    attack_t = [i[0] for i in attacks]
    damage = [i[1] for i in attacks]

    for time in range(1, attack_t[-1]+1):  #attack_t의 마지막이 최대 마지막 공격을 받았을때
        if time not in attack_t:
            if hp < health and hp >= 0:
                hp += x      #hp가 줄어들었을때부터 체력을 x만큼 회복하기 시작
                if heal_time <= t:
                    heal_time += 1
                if heal_time == t:
                    hp += y
                    heal_time = 0 #heal_time 초기화 안해주면 계속 y만큼 더 회복함

            if hp > health:
                hp = health

        else:   #현재 time이 attack_t에 있는 경우
            hp = hp - damage[attack_t.index(time)]
            heal_time = 0

        if hp <= 0:  #타임 돌기 전에 최종 hp를 확인하여 0보다 작으면 -1을 리턴해서 끝내버림
            return -1
    return hp
