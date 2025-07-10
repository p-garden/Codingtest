a = int(input())
stack = []
for _ in range(a):
    num = int(input())
    if num != 0:
        stack.append(num)
    else:
        stack.pop()

total = sum(stack)
print(total)

