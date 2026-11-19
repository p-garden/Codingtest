from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque()
    tot_weight=0
    tot_len=0
    tot_sec=0
    i=0
    while queue or i<len(truck_weights):
        tot_sec+=1
        
        if queue and queue[0][1]+ bridge_length ==tot_sec:
            tot_weight-= queue[0][0]
            tot_len-=1
            queue.popleft()
            
        if i<len(truck_weights) and(tot_weight+truck_weights[i] <= weight) and (tot_len+1 <= bridge_length):
            queue.append((truck_weights[i],tot_sec))
            tot_weight+=truck_weights[i]
            tot_len+=1
            i+=1
        
    return tot_sec