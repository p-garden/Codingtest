from collections import deque

def solution(priorities, location):
    answer = 1
    queue = deque(range(len(priorities)))
    
    while queue:
        max_pri = max(priorities[idx] for idx in queue)
        max_ind = next(
            i for i, idx in enumerate(queue)
            if priorities[idx] == max_pri
        )
        
        for i in range(0,max_ind):
            a=queue.popleft()
            queue.append(a)
            
        exit = queue.popleft()
        if exit ==location:
            return answer
        answer+=1