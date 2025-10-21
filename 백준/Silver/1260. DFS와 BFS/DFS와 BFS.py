import sys
from collections import deque
input = sys.stdin.readline
n,m,s = map(int, input().split(' '))
graph = [[] for _ in range(n+1) ]
for _ in range(m):
  u,v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)
for i in range(1,n+1):
  graph[i].sort()

visited_dfs = [False]*(n+1)
def dfs(graph,s,visited):
  print(s, end=' ')
  visited[s] = True
  for j in graph[s]:
    if not visited[j]:
      dfs(graph,j,visited)
visited_bfs = [False]*(n+1)

def bfs(graph,s,visited):
  queue = deque()
  queue.append(s)
  while queue:
    value = queue.popleft()
    if not visited[value]:
      print(value, end= ' ')
      visited[value] = True
      for j in graph[value]:
        queue.append(j)
    

dfs(graph,s,visited_dfs)
print()
bfs(graph, s, visited_bfs)