from itertools import permutations
def solution(k, dungeons):
    answer = 0
    for p in permutations(dungeons,len(dungeons)):
        obj = k
        current =0
        for need,use in p:
            if obj >= need:
                current+=1
                obj -= use
        answer = max(answer,current)
    return answer