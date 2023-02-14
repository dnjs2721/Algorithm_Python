import sys

N = int(sys.stdin.readline().rstrip())
oasis = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

stack = [] # (키, count)
res = 0

for i in oasis:
    # 스택 끝 키 값보다 키가 크면
    while stack and stack[-1][0] < i: 
        # res += pop()의 count값 
        res += stack.pop()[1]

    # 스택이 비어있으면 (키, 1) append
    if not stack:
        stack.append((i,1))
        continue

    # 스택 끝 값의 키와 같을 때
    elif stack[-1][0] == i:
        cnt = stack.pop()[1]
        res += cnt
    
        if stack:
            res += 1
        stack.append((i, cnt + 1))
    
    else:
        stack.append((i, 1))
        res += 1

print(res)