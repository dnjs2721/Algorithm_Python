import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    while fire_q:
        x, y = fire_q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or nx >= h or 0 > ny or ny >= w:
                continue
            if dist[nx][ny] == '#' or fire_visted[nx][ny] != 0:
                continue
            fire_visted[nx][ny] = fire_visted[x][y] + 1
            fire_q.append((nx, ny))
    
    while user_q:
        x, y = user_q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or nx >= h or 0 > ny or ny >= w:
                return user_visted[x][y] + 1
            if dist[nx][ny] == '#' or user_visted[nx][ny] != 0 or (fire_visted[nx][ny] != 0 and fire_visted[nx][ny] <= user_visted[x][y] + 1):
                continue
            if dist[nx][ny] == '*':
                continue
            user_visted[nx][ny] = user_visted[x][y] + 1
            user_q.append((nx, ny))
    return 'IMPOSSIBLE'


t =  int(input())
for _ in range(t):
    w, h = map(int,input().split())
    dist = [list(input().rstrip()) for _ in range(h)]
    fire_visted, user_visted = [[0]*w for _ in range(h)], [[0]*w for _ in range(h)]
    fire_q, user_q = deque(), deque()

    for i in range(h):
        for j in range(w):
            if dist[i][j] == '*':
                fire_q.append((i,j))
            if dist[i][j] == '@':
                user_q.append((i,j))
    print(bfs())