import sys
from collections import deque
input = sys.stdin.readline

n, m, h = map(int,input().rstrip().split())
tomato = []
for _ in range(h):
    dist = []
    for _ in range(m):
        dist.append(list(map(int, input().rstrip().split())))
    tomato.append(dist)

q = deque()

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

count = 0 

for i in range(h):
    for j in range(m):
        for k in range(n):
            if tomato[i][j][k] == 1:
                q.append((i, j , k))

def bfs():
    while q:
        z, y, x = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and tomato[nz][ny][nx] == 0:
                tomato[nz][ny][nx] = tomato[z][y][x] + 1 
                q.append((nz, ny, nx))

bfs()
for i in tomato:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
            count = max(count, k)

print(count - 1)