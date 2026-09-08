def solution(n, lost, reserve):
    #lost와 reserve의 중복 학생 제거 및 각 리스트에서 중복 경우 없으니 집합 사용
    lost = set(lost)
    reserve = set(reserve)
    diff = reserve & lost
    lost -= diff
    reserve -= diff
    
    answer = n-len(lost)
    for i in sorted(lost):
        if (i-1) in reserve:
            reserve.remove(i-1)
            answer += 1
        elif (i+1) in reserve:
            reserve.remove(i+1)
            answer+=1
    return answer

