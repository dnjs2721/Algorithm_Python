from collections import deque

dx = [0, 0 ,1, -1]
dy = [1, -1, 0, 0]

def solution(maps):
    for i in range(len(maps)):
        for j in range(len((maps[0]))):
            if maps[i][j] == 'S':
                return(bfs(i, j, maps))
                
def bfs(i, j, maps):
    q = deque()
    q.append((i,j))
    visit = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    visit[i][j] = 1
    flag = False
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= len(maps[0]) or ny >= len(maps) or visit[ny][nx] != 0:
                continue
            if maps[ny][nx] == 'X':
                continue
            elif maps[ny][nx] == 'L':
                q.clear()
                q.append((ny, nx))
                tmp = visit[y][x] + 1
                visit = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
                visit[ny][nx] = tmp
                flag = True
                break
            elif maps[ny][nx] == 'E' and flag == True:
                return visit[y][x]
                             
            q.append((ny, nx))
            visit[ny][nx] = visit[y][x] + 1

    return -1
            
print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))