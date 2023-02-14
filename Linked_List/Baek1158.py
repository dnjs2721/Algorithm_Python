import sys
N, K = map(int,sys.stdin.readline().strip().split())
arr = [i for i in range(1, N+1)]
stack = []
num = 0
for i in range(N) :
    num += K-1
    if num >= len(arr):
        num = num%len(arr)

    stack.append(str(arr.pop(num)))

print("<",", ".join(stack),">",sep='')