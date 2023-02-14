import sys

N =  int(sys.stdin.readline())
res = 0

for _ in range(N):
    arr =  sys.stdin.readline().rstrip()
    stack = []

    for i in arr:
        if stack:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)
        
    if len(stack) == 0:
        res += 1

print(res)