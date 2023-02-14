import sys
from collections import deque
input = sys.stdin.readline

f, s, g, u, d = map(int, input().rstrip().split())
dist = [0 for _ in range(f)]
q = deque()
dx = [u, -d]

def bfs(v):
    q.append(v)
    dist[v] = 1
    while q:
        x = q.popleft()
        if x == g-1:
            return dist[g-1] - 1
        for i in range(2):
            nx = x + dx[i]
            if 0 <= nx < f and dist[nx] == 0:
                dist[nx] = dist[x] + 1
                print(dist)
                q.append(nx)
    if dist[g-1] == 0:
        return "use the stairs"

print(bfs(s-1))