import sys
input = sys.stdin.readline
s = input().rstrip()
result = list()
stack = list()
tag=False

for ch in s:
  if ch =='<':
    while stack:
      result.append(stack.pop())
    tag=True
    result.append(ch)
  elif ch == '>':
    tag = False
    result.append(ch)
  elif tag:
    result.append(ch)
  else:
    if ch == ' ':
      while stack:
        result.append(stack.pop())
      result.append(' ')
    else:
      stack.append(ch)
while stack:
  result.append(stack.pop())

print(''.join(result))