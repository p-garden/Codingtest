n = int(input())
for _ in range(n):
    ps = input()
    stack = []
    is_vps = True

    for a in ps:
        if a == '(':
            stack.append('(')
        else: 
            if stack:
                stack.pop()
            else:
                is_vps = False
                break
    if stack:
        is_vps = False
    print('YES' if is_vps else 'NO')
