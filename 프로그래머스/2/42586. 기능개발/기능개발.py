import math
def solution(progresses, speeds):
    answer = []
    days=[]
    for p,s in zip(progresses,speeds):
        remain = math.ceil((100 - p) / s)
        days.append(remain)
    cnt=1
    comp = days[0]
    
    for day in days[1:]:
        if day <= comp:
            cnt+=1
        else:
            answer.append(cnt)
            cnt=1
            comp=day
    answer.append(cnt)
    return answer