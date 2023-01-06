from sys import stdin
from collections import deque
input = stdin.readline

dx = [1, -1, 0, 0 ]
dy = [0, 0, 1, -1]

n, m, k = map(int, input().split())

dist = [list(map(int, input().rstrip())) for _ in range(n)]
visit = [[k+1 for _ in range(m)] for _ in range(n)]
visit[0][0] = 0
def bfs():
    q = deque()
    q.append((0, 0, 0))
    res = 1
    day = True
    while q:
        for _ in range(len(q)):
            x, y, z = q.popleft()
            if x == n-1 and y == m-1:
                return res
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m or visit[nx][ny] <= z:
                    continue
                if dist[nx][ny] == 0:
                    q.append((nx, ny, z))
                    visit[nx][ny] = z
                elif z < k:
                    if not day:
                        q.append((x, y, z))
                    else:
                        visit[nx][ny] = z
                        q.append((nx, ny, z+1))
        res += 1
        day = not day
    return -1

print(bfs())