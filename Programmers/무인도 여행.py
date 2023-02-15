from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = deque()

def solution(maps):
    maps = [list(map(str, i)) for i in maps]
    answer = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'X':
                continue
            answer.append(bfs(maps, i, j,int(maps[i][j])))
    
    return sorted(answer) if len(answer) != 0 else [-1]
            
def bfs(maps, a, b, value):
    q.append((a, b))
    maps[a][b] = 'X'
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= len(maps[0]) or ny >= len(maps) or nx < 0 or ny < 0:
                continue
            if maps[ny][nx] == 'X':
                continue
            value += int(maps[ny][nx])
            q.append((ny, nx))
            maps[ny][nx] = 'X'
            
    return value

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))
print(solution(["XXX","XXX","XXX"]))