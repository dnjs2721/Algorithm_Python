import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    count = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and dist[nx][ny] == 0:
                dist[nx][ny] = 1
                count += 1
                q.append((nx, ny))
    cnt.append(count)

m, n, k = map(int,input().split())
dist = [[0]*(n) for _ in range(m)]
q = deque()
cnt = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(k):
    ly, lx, ry, rx = map(int, input().split())
    for i in range(lx, rx):
        for j in range(ly, ry):
            dist[i][j] = 1

for i in range(m):
    for j in range(n):
        if dist[i][j] == 0:
            dist[i][j] = 1
            q.append((i,j))
            bfs()

cnt.sort()
print(len(cnt))
print(*cnt)