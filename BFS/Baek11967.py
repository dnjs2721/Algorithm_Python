# 내가 불을 켠 곳이 현재는 내 위치에서 떨어져 있는 곳이지만 나중에 방들의 불을 켜며 연결될 수 있기 때문에 체크 맵을 하나만 사용하면 안된다.
# 방문 표시만 하는 visted 배열과 불을 켰는지 여부를 표시하는 lights 배열을 따로 만들어 두 개의 맵을 각각 운영하는 것
# 큐에서 꺼낸 값에 대해 두번의 검사가 필요
    # 딕셔너리에 저장한 정보를 참고해 현 위치에서 불 켤 수 있는 곳을 방문하여 불을 새로 켤 수 있는 곳을 켜고 (result += 1), light에 표시한다.
        # 새로 불을 켠 방의 상하좌우 4방향 연결된 곳을 탐색하며 방문한 적이 있다면, 재검사의 대상이 되므로 큐에 추가
    # 현재 위치에서 4방향 연결된 위치를 확인하며 첫 방문인데 이미 불이 켜진 곳이라면 재검사의 대상이 되므로 큐에 추가
# 큐에 담긴 값에 대한 모든 검사가 끝나면, 불을 켠 방의 갯수를 리턴한다.

from sys import stdin
from collections import deque, defaultdict
input = stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    result = 1 # 결과 값, 불 켤 수 있는 방의 갯수
    visted = [[0] * n for _ in range(n)] # 방문 표시
    visted[0][0] = 1
    lights = [[0] * n for _ in range(n)] # 불 켠 방을 표시
    lights[0][0] = 1
    q = deque([(0, 0)])
    while q:
        x, y = q.popleft()
        for a, b in turninfo[(x, y)]: # 딕셔너리를 참조하여 불 켤 수 있는 곳을 확인
            if not lights[a][b]:
                lights[a][b] = 1 # 새로 불 켜기
                result += 1
                for i in range(4): # 새로 불은 켠 방 기준으로 4방향이 연결된 곳
                    nx = a + dx[i]
                    ny = b + dy[i]
                    if not (0 <= nx < n and 0 <= ny < n): 
                        continue
                    if visted[nx][ny]:# 방문한 적 있으면 (새로 연결되어 또 불을 켤 곳이 있을 수 있으므로)
                        q.append((nx, ny)) # 큐에 담기
        
        # 현 위치를 기준으로
        for i in range(4): # 4방향 연결된 곳
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            # 첫 방문인데 이미 불 켜진 곳이면
            if not visted[nx][ny] and lights[nx][ny]:
                q.append((nx, ny)) # 재검사를 위해 큐에 담기
                visted[nx][ny] = 1 # 방문 표시
    
    return result

n, m = map(int,input().split())
turninfo = defaultdict(list) # 각 위치에서 불 켤 수 있는 위치 정보 저장
for _ in range(m):
    x, y, a, b = map(int,input().split())
    turninfo[(x-1, y-1)].append((a-1, b-1))

print(bfs())