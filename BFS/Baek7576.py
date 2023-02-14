import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
tomato = []

# 좌표를 넣기 위한 []
q = deque([])

# 토마토 받아서 넣기, 이차원 리스트
for i in range(m):
    tomato.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 방향 리스트, [dx[0], dy[0]]은 [0, 1] 아래로 이동
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 정답 변수
count = 0

# q에 처음 토마토가 담긴 위치들을 추가
for i in range(m):
    for j in range(n):
        if tomato[i][j] == 1:
            q.append([i, j])

def bfs():
    # q 가 빌때까지 반복
    while q:
        # q의 왼쪽, 즉 처음 토마토가 담긴 위치를 꺼낸다
        x, y = q.popleft()
        # 위에서 뽑은 좌표를 기준으로 위, 아래, 우, 좌 순으로 찾아본다.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 해당 좌표가 토바토 박스의 크기를 넘어가면 안되며, 그 좌표에 익지 않은 토마토가 있을 때
            if 0 <= nx < m and 0 <= ny < n and tomato[nx][ny] == 0:
                # 해당 위치에 기존 좌표의 크기에 1을 더한 수를 입력한다.
                tomato[nx][ny] = tomato[x][y] + 1
                # 해당 위치를 q에 다시 넣어 반복한다
                for i in tomato:
                    print(i)
                print("-------------------------------")
                q.append([nx, ny])

bfs()
for i in tomato:
    for j in i:
        # 만약 토마토 박스 안애 0이 있다면 익지 않은 토마토가 있다는 것이기에 -1을 출력한다
        if j == 0:
            print(-1)
            exit(0)
    # 0이 없다면 다 익었다는 것이기에 최댓값을 구한다.
    count = max(count, max(i))

# 처음 시작이 1로 시작하기에 1을 빼준다.
print(count - 1)