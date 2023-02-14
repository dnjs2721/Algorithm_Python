import sys
N = int(sys.stdin.readline().rstrip())
stack = []
result = 0

for i in range(N):
    height = int(sys.stdin.readline().rstrip())
    if stack:
        while stack[-1] <= height:
            stack.pop()
            if not stack:
                break
    result += len(stack)
    stack.append(height)

print(result)