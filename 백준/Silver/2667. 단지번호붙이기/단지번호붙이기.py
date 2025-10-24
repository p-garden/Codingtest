import sys
from collections import deque
input = sys.stdin.readline
def bfs(n,apt,i,j):
  count=1
  queue = deque([(i,j)])
  apt[i][j] = 0
  dr = [-1,1,0,0]
  dc = [0,0,-1,1]
  while queue:
    r,c = queue.popleft()

    for i in range(4):
      nr = dr[i]+r
      nc = dc[i]+c
      if (0<= nr < n and 0<= nc < n):
        if apt[nr][nc] ==1:
          apt[nr][nc] =0
          count += 1
          queue.append((nr,nc))
  return count
    

n = int(input())

apt = []
for _ in range(n):
  line = list(map(int, list(input().strip())))
  apt.append(line)

answer = []


for i in range(n):
  for j in range(n):
    if apt[i][j] == 1:
      size = bfs(n,apt,i,j)
      answer.append(size)

print(len(answer))
answer.sort()
for i in range(len(answer)):
  print(answer[i])
      