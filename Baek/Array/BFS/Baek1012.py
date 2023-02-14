import sys
from collections import deque

input = sys.stdin.readline

t = int(input().rstrip())

def bfs(a, b):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    q = deque()
    q.append((a, b))
    dist[a][b] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny <0 or ny >= n:
                continue
            if dist[nx][ny] == 1:
                dist[nx][ny] =0
                q.append((nx, ny))
                

for _ in range(t):
    cnt = 0
    n, m, k = map(int, input().rstrip().split())
    dist = [[0] * n for _ in range(m)]
    for _ in range(k):
        y, x = map(int, input().rstrip().split())
        dist[x][y] = 1
    for i in range(m):
        for j in range(n):
            if dist[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)