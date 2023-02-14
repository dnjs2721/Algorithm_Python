import sys
K = int(sys.stdin.readline().strip())
stack = []
for _ in range(K):
    n = int(sys.stdin.readline().strip())
    if n == 0 :
        if stack:
            stack.pop(-1)
    else :
        stack.append(n)
print(sum(stack))