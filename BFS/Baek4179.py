import sys
from collections import deque
input = sys.stdin.readline
 
def bfs():
    while f_queue:    # fire BFS
        x, y = f_queue.popleft()
 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
 
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
 
            if f_visited[nx][ny] != 0 or graph[nx][ny] == '#':
                continue
 
            f_visited[nx][ny] = f_visited[x][y] + 1
            f_queue.append((nx, ny))
 
    while j_queue:    # jihoon BFS
        x, y = j_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
 
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                return j_visited[x][y] + 1    # escape map
 
            if j_visited[nx][ny] != 0 or graph[nx][ny] == '#' or (f_visited[nx][ny] != 0 and f_visited[nx][ny] <= j_visited[x][y]+1):    # important code
                continue
 
            j_visited[nx][ny] = j_visited[x][y] + 1
            j_queue.append((nx, ny))
 
    return 'IMPOSSIBLE'    # not escape map
 
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
 
n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
f_queue, j_queue = deque(), deque()    # declare fire, jihoon queue
f_visited, j_visited = [[0] * m for _ in range(n)], [[0] * m for _ in range(n)]    # declare fire, jihoon visited
 
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'F':
            f_queue.append((i, j))
        elif graph[i][j] == 'J':
            j_queue.append((i, j))
print(bfs())