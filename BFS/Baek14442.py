import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m, k = map(int, input().split())

dist = [list(map(int, input().rstrip())) for _ in range(n)]
visit = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]

def bfs():
    q = deque()
    q.append((0, 0, k))
    visit[0][0][k] = 1
    while q:
        x, y, z = q.popleft()
        if x == n-1 and y == m-1:
            return visit[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if dist[nx][ny] == 1 and z > 0 and visit[nx][ny][z-1] == 0:
                    visit[nx][ny][z-1] = visit[x][y][z] + 1
                    q.append((nx, ny, z-1))
                elif dist[nx][ny] == 0 and visit[nx][ny][z] == 0:
                    visit[nx][ny][z] = visit[x][y][z] + 1
                    q.append((nx, ny, z))
    return -1

print(bfs())