from collections import deque
def solution(n, m, x, y, r, c, k):
    visted = [[0 for _ in range(m)] for _ in range(n)]
    command = [['' for _ in range(m)] for _ in range(n)]

    dt = [(0, 1, 'd'), (-1, 0, 'l'), (1, 0, 'r'), (0, -1, 'u')]

    q = deque()
    q.append((x - 1, y - 1))
    while q:
        sy, sx = q.popleft()
        if ((r-1) == sy and (c-1) == sx) and (k - visted[sy][sx]) % 2 == 1:
            return 'impossible'
        if ((r-1) == sy and (c-1) == sx) and k == visted[sy][sx]:
            return command[sy][sx]
        for i in range(4):
            dx, dy, com = dt[i]
            nx = sx + dx
            ny = sy + dy
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if visted[sy][sx] + abs(r-1-ny) + abs(c-1-nx) + 1 > k:
                continue
            visted[ny][nx] = visted[sy][sx] + 1
            command[ny][nx] = command[sy][sx] + com
            q.append((ny, nx))
            break

    return 'impossible'


print(solution(3, 4, 2, 3, 3, 1, 5))
print(solution(3, 3, 1, 2, 3, 3, 4))