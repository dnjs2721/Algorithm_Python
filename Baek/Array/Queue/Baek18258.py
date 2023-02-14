import sys
from collections import deque

N = int(sys.stdin.readline())
Q = deque()
res = []

for i in range(N):
    com = sys.stdin.readline().split()
    if com[0] == "push":
        Q.append(int(com[1]))
    elif com[0] == "pop":
        if Q:
            res.append(Q.popleft())
        else:
            res.append(-1)
    elif com[0] == "size":
        res.append(len(Q))
    elif com[0] == "empty":
        if Q:
            res.append(0)
        else:
            res.append(1)
    elif com[0] == "front":
        if Q:
            res.append(Q[0])
        else:
            res.append(-1)
    elif com[0] == "back":
        if Q:
            res.append(Q[-1])
        else:
            res.append(-1)
for i in res:
    print(i)