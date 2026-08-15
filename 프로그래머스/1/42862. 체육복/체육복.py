def solution(n, lost, reserve):
    
    lost = set(lost)
    reserve = set(reserve)
    
    diff = lost & reserve
    lost -= diff
    reserve -= diff
    
    answer = n - len(lost)
    
    for i in sorted(lost):
        sub1 = i - 1
        sub2 = i + 1
        if sub1 in reserve:
            lost.remove(i)
            reserve.remove(sub1)
            answer += 1
        elif sub2 in reserve:
            lost.remove(i)
            reserve.remove(sub2)
            answer += 1
            
    return answer