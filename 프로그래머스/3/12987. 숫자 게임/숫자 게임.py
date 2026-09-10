def solution(A, B):
    answer = 0
    A_point=0
    B_point=0
    A.sort(reverse=True)
    B.sort(reverse=True)
    n=len(A)
    while A_point<n:
        if B[B_point]>A[A_point]:
            B_point+=1
            A_point+=1
            answer+=1
        else:
            A_point+=1
        
    return answer