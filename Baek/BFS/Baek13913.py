import sys
from collections import deque
input = sys.stdin.readline

max = 100001
dist = [0] * max
move = [0] * max
n, k = map(int, input().split())

def path(x):
    arr = []
    temp = x
    for _ in range(dist[x] + 1):
        arr.append(temp)
        temp = move[temp]
    print(' '.join(map(str, arr[::-1])))

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            path(x)
            break
        for nx in (x + 1, x - 1, x * 2):
            if 0 <= nx < max and dist[nx] == 0:
                dist[nx] = dist[x] + 1
                q.append(nx)
                move[nx] = x

bfs()