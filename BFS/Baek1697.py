import sys
from collections import deque
input = sys.stdin.readline
max = 10 ** 5
dist = [0] * (max + 1)
n, k = map(int, input().split())

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            break
        for nx in (x-1, x + 1, x * 2):
            if 0 <= nx <= max and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)

bfs()