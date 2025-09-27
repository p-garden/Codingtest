import sys
input = sys.stdin.readline

n= int(input())
a = list(input().split())

a_cnt=dict()
for t_a in a:
  if t_a in a_cnt:
    a_cnt[t_a] +=1
  else:
    a_cnt[t_a]=1

m= int(input())
b = list(input().split())

for t_b in b:
  if t_b in a_cnt:
    print(a_cnt[t_b], end=' ')
  else:
    print(0, end = ' ')