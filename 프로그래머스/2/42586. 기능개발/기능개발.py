'''
모범답안 -(p-100)//s -> ceil사용안하고 올림 연산 가능
Q[-1][0]에 남은 일자 계산 / [-1][1]를 로 사용
'''

def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]