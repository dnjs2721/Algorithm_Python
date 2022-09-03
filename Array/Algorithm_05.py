import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
V = int(sys.stdin.readline())

res =0

left, right = 0, N

while left < right :
    if arr[left] == V:
        res += 1
    left += 1

print(res)