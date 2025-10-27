import sys
input =sys.stdin.readline

n = int(input())
adj = []
for _ in range(n): 
  line = list(map(int, list(input().split())))
  adj.append(line)


for k in range(n):
  for i in range(n):
    for j in range(n):
      if adj[i][k] == 1 and adj[k][j] ==1:
        adj[i][j] =1
        
for i in range(n):
  print(' '.join(map(str, adj[i])))