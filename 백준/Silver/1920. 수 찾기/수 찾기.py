import sys
input = sys.stdin.readline

n = int(input())
input_list = input().split()
a = set(input_list)

m = int(input())
input_list = input().split()
b = list(input_list)

for b_e in b:
  if b_e in a:
    print('1')
  else:
    print('0')

