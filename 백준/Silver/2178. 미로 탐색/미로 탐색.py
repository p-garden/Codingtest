import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
maze = []
for _ in range(n):
  line = list(map(int, list(input().strip())))
  maze.append(line)
dr = [-1,1,0,0]
dc=[0,0,-1,1]
queue = deque([(0, 0)])

while queue:
  r,c = queue.popleft()
  if (r == (n-1) and c == (m-1)):
    print(maze[r][c])
    break

  for i in range(4):
    nr = r+dr[i]
    nc = c+dc[i]
    if 0 <= nr <n and 0<= nc < m:
      if maze[nr][nc] ==1:
        maze[nr][nc] = maze[r][c] +1
        queue.append((nr,nc))
