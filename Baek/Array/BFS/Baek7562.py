import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

dx = [1, 2, 1, 2, -1, -2, -1, -2]
dy = [2, 1, -2, -1, 2, 1, -2, -1]

def bfs(a, b, c, d):
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        if x == c and y == d:
            print(dist[c][d])
            return
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and dist[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))


for _ in range(t):
    l = int(input())
    start_x, start_y = map(int,input().split())
    end_x, end_y = map(int,input().split())
    dist = [[0]*l for _ in range(l)]
    bfs(start_x, start_y, end_x, end_y)