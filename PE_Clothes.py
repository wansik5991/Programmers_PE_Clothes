import os
os.system('cls')

def solution(n, lost, reserve):

    lost.sort()
    student = [0] + [1] * n + [0]
    
    for i in range(len(lost)) :
        if lost[i] in reserve :
            reserve[reserve.index(lost[i])] = 0
            lost[i] = 0
    
    for i in reserve :
        student[i] = 2
    for i in lost :
        student[i] = 0

    student[0] = 0
    
    for i in lost :
        if student[i-1] == 2 :
            student[i-1], student[i] = 1,1
        elif student[i+1] == 2 :
            student[i+1], student[i] = 1,1

    answer = n-(student.count(0)-2)
    return answer

print(solution(5, [1,2,3], [2,3,4]))
print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2,4], [3]))
print(solution(3, [3], [1]))
