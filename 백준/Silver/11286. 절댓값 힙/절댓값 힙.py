import sys, heapq
input = sys.stdin.readline

N = int(input())
x = []

for i in range(N):
    temp = int(input()) 
    if temp ==0:
        if x:
            print(heapq.heappop(x)[1])
        else:
            print(0)
    else:
        heapq.heappush(x,(abs(temp),temp))
