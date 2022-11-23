import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())
position = list(map(int, sys.stdin.readline().split()))
q = deque([i for i in range(1, n+1)])

count = 0

for i in position:
    while True:
        if q[0] == i:
            q.popleft()
            break
        else:
            if q.index(i) < len(q)/2:
                while q[0] != i:
                    q.rotate(-1)
                    count += 1
            else:
                while q[0] != i:
                    q.rotate(1)
                    count += 1

print(count)