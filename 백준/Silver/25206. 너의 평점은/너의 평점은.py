grade_list = []
sum_score = 0
for _ in range(20):
    title, score, grade = input().split()
    score = float(score)
    if grade != 'P':
        sum_score += score
        if grade == 'A+':
            grade_list.append(score * 4.5)
        elif grade == 'A0':
            grade_list.append(score * 4.0)
        elif grade == 'B+':
            grade_list.append(score * 3.5)
        elif grade == 'B0':
            grade_list.append(score * 3.0)
        elif grade == 'C+':
            grade_list.append(score * 2.5)
        elif grade == 'C0':
            grade_list.append(score * 2.0)
        elif grade == 'D+':
            grade_list.append(score * 1.5)
        elif grade == 'D0':
            grade_list.append(score * 1.0)
        else:
            grade_list.append(0.0)

print(sum(grade_list) / sum_score)