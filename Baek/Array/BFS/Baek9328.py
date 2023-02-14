from sys import stdin
from collections import deque
input = stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    q = deque()
    q.append((0,0))
    visit[0][0] = 0
    kq = [deque() for _ in range(26)]
    res = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h + 2 and 0 <= ny < w + 2:
                if dist[nx][ny] == '*': # 벽
                    continue

                if visit[nx][ny] == -1: # 미방문한 곳 일 때
                    visit[nx][ny] = 0 # 방문 표시

                    if dist[nx][ny] == '$': # 문서를 찾았을 때
                        res += 1 # res += 1

                    elif 'A' <= dist[nx][ny] <= 'Z': # 문 일 때
                        dore = ord(dist[nx][ny]) - ord('A') # dore 는 해당 자리 문의 아스키 코드 값을 가진다
                        if key_st[dore] is False: # 만약 dore에 해당하는 키가 없을 때
                            kq[dore].append((nx, ny)) # kq에 문의 위치를 기록한다
                            continue

                    elif 'a' <= dist[nx][ny] <= 'z': # 열쇠 일 때
                        key = ord(dist[nx][ny]) - ord('a') # key 는 해당 자리 열쇠의 아스키 코드 값을 가진다.
                        key_st[key] = True # 해당 키의 저장소를 True로 변경한다.
                        while kq[key]: # 만약 해당 키의 문이 기록 되어 있을 때
                            kx, ky = kq[key].popleft()
                            q.append((kx, ky)) # 문의 위치를 q에 추가한다.

                    q.append((nx, ny)) # 미방문인 곳을 추가한다.

    return res

t = int(input())

for _ in range(t):
    h, w = map(int, input().split())

    dist = [list('.' * (w + 2))] # 평면도의 첫 줄 임의로 확장 and 가로로 2칸 확장
    for _ in range(h):
        dist.append(list('.' + input().rstrip() + '.')) # 입력되는 평면도의 양 옆에 . 추가 
    dist.append(list('.' * (w + 2))) # 평면도의 마지막 줄 임의로 확장 and 가로로 2칸 확장

    k = input().rstrip()

    visit = [[-1] * (w + 2) for _ in range(h + 2)] # 평면도가 2열, 2행 추가가 되었기에 방문 체크 배열도 확장
    key_st = [False] * 26 # 열쇠들의 소지 여부를 판단, 처음 가지는 열쇠는 True로 변경

    if k != '0': # 키를 가지고 있다면
        for i in k: # 해당 키의 key_st 인덱스를 True로 변경
            key_st[ord(i) - ord('a')] = True

    print(bfs())