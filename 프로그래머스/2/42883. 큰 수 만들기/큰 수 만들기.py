def solution(number, k):
    answer = ''
    
    for num in number:
        while answer and k>0 and answer[-1] < num:
            answer = answer[:-1]
            k -= 1
        
        answer += num
    if k>0:
        answer = answer[:-k]

    return answer