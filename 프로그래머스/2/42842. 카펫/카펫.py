def solution(brown, yellow):
    answer = []
    n_brown = brown //2 -2 
    for i in range(1,n_brown):
        if i * (yellow // i) == yellow and i+ (yellow // i) == n_brown:
            a=i
            b=yellow // i
            break
    
    a+=2
    b+=2
    if a>=b:
        answer.append(a)
        answer.append(b)
    else:
        answer.append(b)
        answer.append(a)
            
    
    return answer
