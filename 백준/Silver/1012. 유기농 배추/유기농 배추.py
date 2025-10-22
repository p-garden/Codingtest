import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def island(baechu,n,m,k):
  cnt =0
  dr = [-1,1,0,0]
  dc = [0,0,-1,1]
  def dfs(r,c):
    if r<0 or r>=n or c<0 or c>=m or baechu[r][c] ==0:
      return

    baechu[r][c] =0
    for i in range(4):
      nr,nc = r+dr[i] , c+dc[i]
      dfs(nr,nc)

  for i in range(n):
    for j in range(m):
      if baechu[i][j] ==1:
        cnt += 1
        dfs(i,j)
  return cnt
    
t = int(input())
answer = []
for _ in range(t):
  m,n,k = map(int, input().split())
  baechu = [[0]*m for _ in range(n)]
  for _ in range(k):
    j,i = map(int, input().split())
    baechu[i][j] = 1
  result = island(baechu,n,m,k)
  answer.append(result)

for res in answer:
    print(res)  