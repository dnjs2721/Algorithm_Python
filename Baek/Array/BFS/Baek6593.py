import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
        while q:
            z, y, x = q.popleft()
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]
                if nx < 0 or ny < 0  or nz < 0 or nx >= c or ny >= r or nz >= l:
                    continue
                if visited[nz][ny][nx] != 0 or dist[nz][ny][nx] == '#' or dist[nz][ny][nx] == 'S':
                    continue
                visited[nz][ny][nx] = visited[z][y][x] + 1
                q.append((nz, ny, nx))

while True:      
    l, r, c = map(int, input().rstrip().split())
    if l == 0 and r == 0 and c == 0:
        break

    q = deque()
    dist = [[]*r for _ in range(l)]
    visited = [[[0]*c for _ in range(r)] for _ in range(l)]

    for i in range(l):
        for j in range(r):
            dist[i].append(list(input().rstrip()))
        input()
    
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if dist[i][j][k] == 'S':
                    q.append((i, j, k))
                if dist[i][j][k] == 'E':
                    ez, ey, ex = i, j ,k
    
    bfs()
    if visited[ez][ey][ex] == 0:
        print("Trapped!")
    else:
        print(f'Escaped in {visited[ez][ey][ex]} minute(s).')