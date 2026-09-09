def solution(A, B):
    B.sort(reverse=True)
    A.sort(reverse=True)
    A_point=0
    B_point=0
    n = len(B)
    answer = 0
    while A_point < n: 
        if A[A_point] < B[B_point]:
            answer+=1
            A_point+=1
            B_point+=1
        else:
            A_point+=1
            
    return answer