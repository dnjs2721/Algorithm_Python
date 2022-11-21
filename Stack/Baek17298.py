# import sys
# N = int(sys.stdin.readline().strip())
# arr = list(map(int, sys.stdin.readline().strip().split()))
# stack = [-1]*N
# for i in range(N-1):
#     tmp = 1
#     while i+tmp < N:
#         if arr[i] >= arr[i+tmp]:
#             tmp += 1
#         else:
#             stack[i] = arr[i+tmp]
#             break
# print(*stack)

import sys
N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))
res = [-1]*N
stack = []

stack.append(0)
for i in range(1,N):
    while stack and arr[stack[-1]] < arr[i]:
        res[stack.pop()] = arr[i]
    stack.append(i)

print(*res)