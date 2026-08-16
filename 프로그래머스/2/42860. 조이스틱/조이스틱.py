def solution(name):
    answer = 0
    
    #알파벳 이동
    for i in name:
        answer += min(ord(i) - ord('A'),  ord('Z')-ord(i)+1)
    
    #커서 이동
    n_len = len(name)
    min_move = n_len-1
    
    for i in range(n_len):
        next_idx = i+1
        while next_idx < n_len and name[next_idx] == 'A':
            next_idx += 1
            
        min_move = min(min_move, i*2+(n_len-next_idx), (n_len-next_idx)*2+i)
        
    return answer + min_move