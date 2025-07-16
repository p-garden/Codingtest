import sys, heapq
input = sys.stdin.readline
N,ref,lim = map(int, input().split())
giant=[]
for _ in range(N):
    pre = int(input())
    heapq.heappush(giant,-pre)
    
if -giant[0] < ref:
    print('YES')
    print(0)
    sys.exit()
i=0
while i< lim:
    max = -giant[0]
    if max >1:
        heapq.heappop(giant)
        heapq.heappush(giant, -(max//2))
    if (-giant[0]) < ref:
        print('YES')
        print(i+1)
        break
    i += 1

if i == lim:
    print('NO')
    print(int(-heapq.heappop(giant)))

