import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input())
dist = [list(map(int, input().rstrip().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
count = 1
answer = sys.maxsize

def bfs(i, j):
    q = deque()
    global count
    visited[i][j] = 1
    q.append((i, j))
    dist[i][j] = count
    while q:
        y, x = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == 0 and dist[ny][nx] == 1:
                visited[ny][nx] = 1
                dist[ny][nx] = count
                q.append((ny, nx))

def bfs2(num):
    global answer
    arr = [[-1]*n for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(n):
            if dist[i][j] == num:
                q.append((i, j))
                arr[i][j] = 0
    
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if dist[ny][nx] > 0 and dist[ny][nx] != num:
                answer = min(answer, arr[y][x])
                return
            if dist[ny][nx] == 0 and arr[ny][nx] == -1:
                arr[ny][nx] = arr[y][x] + 1
                q.append((ny, nx))

for i in range(n):
    for j in range(n):
        if dist[i][j] == 1 and visited[i][j] == 0:
            bfs(i, j)
            count += 1

for i in range(1, count):
    bfs2(i)

print(answer)