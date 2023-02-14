import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, maxNum, visited):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if dist[nx][ny] > maxNum and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

n = int(input().rstrip())
maxNum = 0
result = []
dist = []

for i in range(n):
    dist.append(list(map(int, input().rstrip().split())))
    for j in range(n):
        if dist[i][j] > maxNum:
            maxNum = dist[i][j]

for i in range(maxNum):
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if dist[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i, visited)
                cnt += 1
    result.append(cnt)

print(max(result))