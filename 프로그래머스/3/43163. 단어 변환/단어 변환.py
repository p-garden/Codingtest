from collections import deque
def solution(begin, target, words):
    def count_len(begin, target):
        cnt=0
        for i in range(len(begin)):
            if begin[i] == target[i]:
                cnt+=1
        return cnt
    
    queue = deque()
    trans = True
    if target not in words:
        return 0
    n = len(words)
    queue.append((begin,0))
    while queue:
        cur,ind = queue.popleft()
        if cur == target:
                return ind
        for word in words:
            if count_len(cur, word) == len(cur)-1:
                queue.append((word,ind+1))
                
    return -1