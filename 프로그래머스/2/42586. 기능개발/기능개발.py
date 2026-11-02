def solution(progresses, speeds):
    answer = []
    tf = 0
    while tf < len(speeds):
        temp=0
        for i in range(len(speeds)):
            progresses[i] += speeds[i]
        if progresses[tf] >= 100:
            temp+=1
            tf+=1
            for j in range(tf,len(speeds)):
                if progresses[j] >= 100:
                    temp +=1 
                    tf+=1
                else:
                    break
        if temp>0:
            answer.append(temp)
    return answer