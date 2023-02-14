import sys

N = int(sys.stdin.readline())
res = []

for _ in range(N):
    arr =  sys.stdin.readline().rstrip()
    stack =  []
    flag = False

    for i in arr:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag =  True
                break
    
    if stack:
        flag = True
    
    if flag:
        res.append("NO")
    else:
        res.append("YES")

for i in res:
    print(i)