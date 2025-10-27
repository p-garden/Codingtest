import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def dfs(square,n,m,i,j):
  square[i][j] = 0
  nr = [-1,1,0,0,-1,-1,1,1]
  nc = [0,0,-1,1,-1,1,-1,1]
  for k in range(8):
    if 0<=(i+nr[k])<n and 0<= (j+nc[k])<m:
      if square[i+nr[k]][j+nc[k]]==1:
        dfs(square,n,m,i+nr[k],j+nc[k])
    

answer = []
while(True):
  cnt =0
  m,n = map(int, input().split())
  if n ==0 and m ==0:
    break
  square = []
  for i in range(n):
    line = list(map(int, list(input().split())))
    square.append(line)
  for i in range(n):
    for j in range(m):
      if square[i][j] ==1:
        cnt += 1
        dfs(square,n,m,i,j)
  answer.append(cnt)
for i in answer:
  print(i)