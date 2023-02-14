from sys import stdin
from collections import deque
input = stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    is_moved = True
    while is_moved:
        is_moved = False
        for i in range(1, p+1):
            if not castle[i]:
                continue
            q = castle[i]
            for _ in range(power[i]):
                if not q:
                    break
                for _ in range(len(q)):
                    x, y = q.popleft()
                    for j in range(4):
                        nx = x + dx[j]
                        ny = y + dy[j]
                        if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == '.':
                            dist[nx][ny] = str(i)
                            q.append((nx, ny))
                            cnt[i] += 1
                            is_moved = True

n, m, p = map(int, input().split())
castle = [deque() for _ in range(p+1)]
power = [0] + list(map(int, input().split()))
dist = [list(input().rstrip()) for _ in range(n)]
cnt = [0]*(p+1)

for i in range(n):
    for j in range(m):
        if dist[i][j] != '.' and dist[i][j] != '#':
            cnt[int(dist[i][j])] += 1
            castle[int(dist[i][j])].append((i,j))

bfs()
print(*cnt[1:])