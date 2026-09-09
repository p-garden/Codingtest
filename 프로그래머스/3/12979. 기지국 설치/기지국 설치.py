import math
def solution(n, stations, w):
    answer = 0
    prev=1
    max_trans = 2*w+1
    for i in stations:
        first = max(i -w,1)
        last = min(i+w,n)
        gap = first - prev
        
        if gap >0:
            answer += math.ceil(gap/max_trans)
        prev = last+1
    gap = n-prev+1
    
    if gap >0:
        answer += math.ceil(gap/max_trans)
            
    return answer
