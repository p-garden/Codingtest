from collections import deque

def solution(priorities, location):
    answer = 1
    queue = deque()
    alpha=0
    for i in priorities:
        queue.append(alpha)
        alpha+=1
    
    while queue:
        max_pri = priorities[queue[0]]
        max_ind=0
        for i in range(len(queue)):
            if max_pri <priorities[queue[i]]:
                max_ind=i
                max_pri = priorities[queue[i]]
        for i in range(0,max_ind):
            a=queue.popleft()
            queue.append(a)
            
        exit = queue.popleft()
        if exit ==location:
            return answer
        answer+=1