import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while fq:
        x, y = fq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if f_visited[nx][ny] != 0 or maze[nx][ny] == '#':
                continue

            f_visited[nx][ny] = f_visited[x][y] + 1
            fq.append((nx, ny))

    while jq:
        x, y = jq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                return j_visited[x][y] + 1
                
            if j_visited[nx][ny] != 0 or maze[nx][ny] == '#' or (f_visited[nx][ny] != 0 and f_visited[nx][ny] <= j_visited[x][y]+1):
                continue

            j_visited[nx][ny] = j_visited[x][y] + 1
            jq.append((nx, ny))
            
    return 'IMPOSSIBLE'

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
maze = [list(input().strip()) for _ in range(n)]
fq, jq = deque(), deque()
f_visited, j_visited = [[0] * m for _ in range(n)], [[0] * m for _ in range(n)]
 
for i in range(n):
    for j in range(m):
        if maze[i][j] == 'F':
            fq.append((i, j))
        elif maze[i][j] == 'J':
            jq.append((i, j))
print(bfs())