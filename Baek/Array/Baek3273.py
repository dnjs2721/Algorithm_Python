# # 시간초과 - 시간복잡도가 O(n^2) 이기 때문에 리스트의 데이터가 커지면 시간 초과
# import sys

# f = int(sys.stdin.readline())
# s = list(map(int, sys.stdin.readline().split()))
# t = int(sys.stdin.readline())

# res = 0

# for i in s:
#     for j in range(1,f):
#         if i + s[j] == t:
#             res += 1
#             break

# print(res//2)

import sys

f = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
t = int(sys.stdin.readline())

s.sort()

left, right = 0, f-1
res = 0

while left < right:
    tmp = s[left] + s[right]
    if tmp > t:
        right -= 1
    elif tmp < t:
        left += 1
    else:
        res += 1
        left += 1
        right -= 1
print(res)