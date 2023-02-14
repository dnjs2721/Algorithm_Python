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
            if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == 1:
                dist[nx][ny] = 0
                count += 1
                q.append((nx, ny))
    cnt.append(count)


n = int(input())
dist = []
cnt = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
q = deque()

for _ in range(n):
    dist.append(list(map(int, input().rstrip())))

for i in range(n):
    for j in range(n):
        if dist[i][j] == 1:
            dist[i][j] = 0
            q.append((i, j))
            bfs()

print(len(cnt))
cnt.sort()
for i in cnt:
    print(i)