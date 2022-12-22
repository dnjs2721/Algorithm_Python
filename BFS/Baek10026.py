import sys
from collections import deque
input = sys.stdin.readline

n =  int(input().rstrip())
dist = [list(input().rstrip()) for _ in range(n)]
q = deque()

def bfs(a, b):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q.append((a, b))
    visted[a][b] = 1
    while q:
        x, y =  q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == dist[x][y] and not visted[nx][ny]:
                visted[nx][ny] = 1
                q.append((nx, ny)) 


# 적록색약이 아닌 경우
visted = [[0] * n for _ in range(n)]
cnt1 = 0
for i in range(n):
    for j in range(n):
        if not visted[i][j]:
            bfs(i, j)
            cnt1 += 1

# 적록색약인 경우
visted = [[0] * n for _ in range(n)]
cnt2 = 0
for i in range(n):
    for j in range(n):
        if dist[i][j] == 'R':
            dist[i][j] = 'G'
for i in range(n):
    for j in range(n):
        if not visted[i][j]:
            bfs(i, j)
            cnt2 += 1

print(cnt1, cnt2)