def solution(k, tangerine):
    #dict 사용시 초기화 + 누적합 : get , sorted와 sort 의 차이
    answer = 0
    tangerine_cnt = dict()
    for i in tangerine:
        tangerine_cnt[i] = tangerine_cnt.get(i,0)+1
        
    counts = sorted(tangerine_cnt.values(), reverse=True)
    
    for cnt in counts:
        if k > 0:
            k -= cnt
            answer += 1
        else:
            break

    return answer