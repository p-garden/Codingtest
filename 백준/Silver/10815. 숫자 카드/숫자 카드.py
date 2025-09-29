import sys
input = sys.stdin.readline

n = int(input())
n_set = set(input().split())

m = int(input())
m_set = list(input().split())

for t_m in m_set:
  if t_m in n_set:
    print('1 ', end = '')
  else:
    print('0 ', end='')