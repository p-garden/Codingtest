import sys,heapq
input = sys.stdin.readline
N= int(input())
x = []
for i in range(N):
    pre = int(input())
    if pre == 0:
        if len(x)==0:
            print(0)
        else:
            print(heapq.heappop(x)[1])
    else:
        heapq.heappush(x,(abs(pre),pre))

