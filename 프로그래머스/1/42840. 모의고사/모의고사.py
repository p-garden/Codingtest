def solution(answers):
    n= len(answers)
    a=[]
    b=[]
    for i in range(1,n+1):
        m = i %5
        if m ==0:
            m =5
        a.append(m)
        

    pattern = [1, 3, 4, 5]
    for i in range(n):
        if i % 2 == 0:
            b.append(2)
        else:
            b.append(pattern[(i // 2) % 4])
            
    pattern = [3, 1, 2, 4, 5]
    c = [pattern[(i // 2) % 5] for i in range(n)]
    
    
    a_cnt, b_cnt, c_cnt = 0, 0, 0
    for i in range(n):
        if answers[i] == a[i]:
            a_cnt+=1
        if answers[i] == b[i]:
            b_cnt+=1
        if answers[i] == c[i]:
            c_cnt+=1
            
    max_p = max(a_cnt,b_cnt,c_cnt)
    answer = []
    if max_p == a_cnt:
        answer.append(1)
    if max_p == b_cnt:
        answer.append(2)
    if max_p == c_cnt:
        answer.append(3)        
    
    return answer