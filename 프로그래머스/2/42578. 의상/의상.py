def solution(clothes):
    answer = 1
    ootd = dict()
    for cloth,clo_type in clothes:
        ootd[clo_type] = ootd.get(clo_type,0)+1
    
    for i in ootd.values():
        answer *= (i+1)
    return answer-1