import sys
input = sys.stdin.readline

n,m = map(int, input().split())

n_set = set()
for _ in range(n):
  string = input().strip()
  n_set.add(string)

m_set = set()
for _ in range(m):
  string = input().strip()
  m_set.add(string)

cnt=0
inter_list = []
for m_t in m_set:
  if m_t in n_set:
    cnt+=1
    inter_list.append(m_t)
inter_list = sorted(inter_list)
print(cnt)
for t in inter_list:
  print(t)