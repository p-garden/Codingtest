from collections import deque

def solution(begin, target, words):
    answer = 0
    queue=deque()
    def check(a,b):
        cnt=0
        for i in range(len(a)):
            if a[i] ==b[i]:
                cnt+=1
        return(cnt == len(a)-1)
    queue.append((begin,0))
    while queue:
        start,dist = queue.popleft()
        if start ==target:
            return dist
        for word in words:
            if check(word,start):
                words.remove(word)
                queue.append((word,dist+1))
    return 0