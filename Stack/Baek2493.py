# 시간초과 O(N^2) index 함수가 해당 원소를 찾기 위해
# 리스트를 처음부터 끝까지 순회
# import sys
# N = int(sys.stdin.readline())
# towers = list(map(int,sys.stdin.readline().strip().split()))
# arr = list(reversed(towers))
# stack = [0]*N

# for i in range(N):
#     tmp = arr.pop(0)
#     print(tmp)
#     for j in arr:
#         if tmp < j:
#             stack[towers.index(tmp)] = towers.index(j)+1
#             break

# print(*stack)

import sys
N = int(sys.stdin.readline())
towers = list(map(int,sys.stdin.readline().strip().split()))
stack = []
arr = [0]*N

for i in range(N):
    while stack:
        if stack[-1][1] > towers[i]:
            arr[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, towers[i]])

print(*arr)