import sys
from collections import deque

N, L = map(int, sys.stdin.readline().rstrip().split())
target = list(map(int, sys.stdin.readline().split()))
q = deque()

for i in range(N):
    
    # 들어갈 숫자보다 큰 것들을 전부 pop 해준다.
    while q and q[-1][0] > target[i]:
        q.pop()

    # i-L+1 인덱스 이전의 것들을 pop해준다.
    while q and q[0][1] < i - L + 1:
        q.popleft()
    q.append((target[i],i))
    print(q[0][0], end=' ')