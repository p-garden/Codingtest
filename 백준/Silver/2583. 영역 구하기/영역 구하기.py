import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def dfs(square,i,j,n,m):
  nr = [-1,1,0,0]
  nc = [0,0,-1,1]
  square[i][j] =1
  size=1
  for k in range(4):
    if (0<=i+nr[k] <n) and (0<=j+nc[k]<m) and square[i+nr[k]][j+nc[k]] ==0:
      size += dfs(square,i+nr[k],j+nc[k],n,m)
  return size


n,m,k = map(int, input().split())
square = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(k):
  x1,y1,x2,y2 = map(int, input().split())
  y1 = n-1-y1
  y2 = n-y2
  x2 -= 1
  for i in range(y2,y1+1):
    for j in range(x1,x2+1):
      square[i][j] = 1
cnt=0
size_list = []
for i in range(n):
  for j in range(m):
    if square[i][j] == 0:
      area_size = dfs(square,i,j,n,m)
      cnt += 1
      size_list.append(area_size)

print(cnt)
size_list.sort()
for size in size_list:
  print(size,end=' ') 
