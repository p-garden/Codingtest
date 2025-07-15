import sys,heapq
input = sys.stdin.readline
N= int(input())
x = []
for i in range(N):
    pre = int(input()) * -1
    heapq.heappush(x,pre)
    if pre == 0:
        print(-heapq.heappop(x))

    

