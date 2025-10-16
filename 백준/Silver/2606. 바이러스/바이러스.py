import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
  u,v = map(int,input().split())
  graph[u].append(v)
  graph[v].append(u)

visited = [False] * (N+1)
count =0

def dfs(node):
  global count
  visited[node]=True
  count += 1
  for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor)
dfs(1)
result = count - 1 if count > 0 else 0
print(result)