import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    q = deque()
    q.append((0, 0, 0))
    while q:
        x, y, z = q.popleft()
        # 끝 점에 도달하면 이동 횟수를 출력
        if x == n-1 and y == m-1:
            return visited[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 다음 이동할 곳이 벽이고, 벽파괴기회를 사용하지 않은 경우
            # 벽이 있다면 z를 1로 변경후 분기
            # 무조건 앞에 나타나는 벽만 부수는게 아닌 4방 중 벽이 아닌 곳이 있다면 아래 조건으로 이동한다.
            if dist[nx][ny] == 1 and z == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                q.append((nx, ny, 1))
            # 다음 이동할 곳이 벽이 아니고, 아직 한 번도 방문하지 않은 경우
            elif dist[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                q.append((nx, ny, z))
    return -1

n, m = map(int, input().rstrip().split())
dist = [list(map(int,input().rstrip())) for _ in range(n)]

# 3차원 행렬을 통해 벽의 파괴를 파악
# visited[x][y][0]은 벽 파괴 가능, [x][y][1]은 불가능을 표현
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

print(bfs())