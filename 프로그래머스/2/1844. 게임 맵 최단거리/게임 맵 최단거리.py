from collections import deque
def solution(maps):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    queue = deque()
    queue.append((0,0,1))
    maps[0][0]=0
    while queue:
        x, y,dist = queue.popleft()
        if x == len(maps)-1 and y==len(maps[0])-1:
            return dist
        for i in range(4):
            nx = x+dx[i]
            ny= y + dy[i]
            if nx>=0 and nx < len(maps) and ny>=0 and ny < len(maps[0]) and maps[nx][ny] ==1:
                maps[nx][ny]=0
                queue.append((nx,ny,dist+1))
    return -1