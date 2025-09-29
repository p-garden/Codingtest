import sys
input = sys.stdin.readline

n,m = map(int, input().split())

n_set= set()
for _ in range(n):
  t_str = input().strip()
  n_set.add(t_str)

m_set= list()
for _ in range(m):
  t_str = input().strip()
  m_set.append(t_str)

cnt=0
for t_m in m_set:
  if t_m in n_set:
    cnt +=1

print(cnt)