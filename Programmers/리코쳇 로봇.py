from collections import deque

def solution(board):
    n = len(board[0])
    m = len(board)
    visted = [[0 for _ in range(n)] for _ in range(m)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def bfs(a, b):
        q = deque([(a, b)])
        while q:
            y, x = q.popleft()
            if board[y][x] == 'G':
                return visted[y][x]
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

    for i in range(m):
        for j in range(n):
            if board[i][j] == 'R':
                return bfs(i, j)

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
print(solution([".D.R", "....", ".G..", "...D"]))
