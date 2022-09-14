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
stack = [-1]*N

for i in range(N-1):
    while i+1 < N:
        if arr[i] >= arr[i+1]:
            arr.pop(i)
        else:
            stack[i]= arr[i+1]
            print(arr)
            print(stack)
            break
print(stack)
