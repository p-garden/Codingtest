def solution(name):
    #각 위치에서 알파벳 이동 횟수는 고정+ A에따른 커서 이동만 변수,name 순회하며 A전 위치에서 A스킵하는 두가지 방법을 고려해 최소 이동 값을 갱신
    alpha =0
    for i in name:
        alpha += min(ord(i)-ord('A'), ord('Z')-ord(i)+1)
    
    n = len(name)
    cursor= n-1
    for i in range(n):
        next_idx =i+1
        while next_idx < n and name[next_idx] =='A':
            next_idx +=1
        cursor = min(cursor, i*2+n-next_idx)
        cursor = min(cursor, (n-next_idx)*2+i)
        
    return alpha+cursor