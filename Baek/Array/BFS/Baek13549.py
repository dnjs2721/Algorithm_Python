import sys
from collections import deque
input = sys.stdin.readline
max = 100001
dist = [0] * 100001

n, k = map(int, input().split())

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            break
        for nx in (x * 2, x - 1, x + 1):
            if 0 <= nx < max and not dist[nx]:
                if nx == x + 1 or nx == x - 1:
                    dist[nx] = dist[x] + 1
                    q.append(nx)
                if nx == x * 2:
                    dist[nx] = dist[x]
                    q.append(nx)

bfs()