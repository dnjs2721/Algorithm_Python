import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    seaList = []
    while q:
        count = 0
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if dist[ny][nx] == 0:
                    count += 1
                elif dist[ny][nx] > 0 and visited[ny][nx] == 0:
                    q.append((ny, nx))
                    visited[ny][nx] = 1
        if count > 0:
            seaList.append((y, x, count))
    for y, x, count in seaList:
        dist[y][x] = max(0, dist[y][x] - count)
    
    return 1

n, m = map(int,input().rstrip().split())
dist = [list(map(int,input().rstrip().split())) for _ in range(n)]
year = 0

ice = []
for i in range(n):
    for j in range(m):
        if dist[i][j]:
            ice.append((i, j))

while True:
    q = deque()
    visited = [[0]*m for _ in range(n)]
    delList = []
    cnt = 0

    for i, j in ice:
        if dist[i][j] > 0 and visited[i][j] == 0:
            q.append((i, j))
            visited[i][j] = 1
            cnt += bfs()
        if dist[i][j] == 0:
            delList.append((i, j))

    if cnt > 1:
        print(year)
        break

    ice = sorted(list(set(ice) - set(delList)))
    year += 1

if cnt < 2:
    print(0)