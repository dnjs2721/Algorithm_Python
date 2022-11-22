import sys
from collections import deque

N = int(sys.stdin.readline())

card = deque()
for i in range(1,N+1):
    card.append(i)

for i in range(N-1):
    card.popleft()
    card.append(card.popleft())

print(card.pop())