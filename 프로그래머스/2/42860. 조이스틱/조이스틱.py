def solution(name):
    answer = 0
    for char in name:
        answer += min(ord(char)-ord('A'), ord('Z') - ord(char) +1)
        
    
    n = len(name)
    min_move = n-1
    
    for i in range(n):
        next = i+1
        while next < n and name[next] =='A':
            next +=1
        min_move = min(min_move, (n-next)*2+i, (n-next)+i*2)
    
    return answer+min_move