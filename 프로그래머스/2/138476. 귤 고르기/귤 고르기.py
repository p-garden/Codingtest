from collections import Counter
def solution(k, tangerine):
    answer = 0
    count = Counter(tangerine)
    count = sorted(count.values(), reverse=True)
    for i in count:
        k -= i
        answer += 1
        if k <= 0:
            break
    return answer