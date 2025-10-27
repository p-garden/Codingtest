import sys
import copy
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def dfs(rain,i,j,k):
  nr = [-1,1,0,0]
  nc= [0,0,-1,1]
  n = len(rain)
  rain[j][k] = i
  for l in range(4):
    if (0<= j +nr[l]<n) and (0<= k+nc[l] < n):
      if rain[j+nr[l]][k+nc[l]] >i:
        dfs(rain,i,j+nr[l],k+nc[l])

n = int(input())
rain = []
for _ in range(n):
  line = list(map(int, list(input().split())))
  rain.append(line)
maxx = max(e for row in rain for e in row)
max_island =1
for i in range(1,maxx+1):
  temp_rain = copy.deepcopy(rain)
  count =0
  for j in range(n):
    for k in range(n):
      if temp_rain[j][k] > i:
        dfs(temp_rain,i,j,k)
        count += 1
  max_island = max(max_island, count)

print(max_island)