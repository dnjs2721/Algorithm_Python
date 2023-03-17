from collections import deque

def solution(board):
    answer = -1
    n = len(board[0])
    m = len(board)
    visted = [[0 for _ in range(n)] for _ in range(m)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def bfs(a, b, c, d):
        q = deque()
        q.append((a, b))
        visted[a][b] = 1
        while q:
            y, x = q.popleft()
            if y == c and x == d:
                return visted[c][d] - 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m or board[ny][nx] == 'D':
                    continue
                while True:
                    nx += dx[i]
                    ny += dy[i]
                    if nx < 0 or ny < 0 or nx >= n or ny >= m or board[ny][nx] == 'D':
                        if visted[ny - dy[i]][nx - dx[i]]:
                            break
                        visted[ny - dy[i]][nx - dx[i]] = visted[y][x] + 1
                        q.append((ny - dy[i], nx - dx[i]))
                        break
        return -1

    sx, sy = 0, 0
    gx, gy = 0, 0

    for i in range(m):
        for j in range(n):
            if board[i][j] == 'R':
                sy, sx = i, j
            elif board[i][j] == 'G':
                gy, gx = i, j

    return bfs(sy, sx, gy, gx)


print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
print(solution([".D.R", "....", ".G..", "...D"]))
