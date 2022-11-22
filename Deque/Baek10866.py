import sys
from collections import deque

N = int(sys.stdin.readline())

q = deque()
res = []

for i in range(N):
    com = sys.stdin.readline().split()
    
    if com[0] == "push_front":
        q.appendleft(int(com[1]))
    elif com[0] == "push_back":
        q.append(int(com[1]))
    elif com[0] == "pop_front":
        if q:
            res.append(q.popleft())
        else:
            res.append(-1)
    elif com[0] == "pop_back":
        if q:
            res.append(q.pop())
        else:
            res.append(-1)
    elif com[0] == "size":
        res.append(len(q))
    elif com[0] == "empty":
        if q:
            res.append(0)
        else:
            res.append(1)
    elif com[0] == "front":
        if q:
            res.append(q[0])
        else:
            res.append(-1)
    elif com[0] == "back":
        if q:
            res.append(q[-1])
        else:
            res.append(-1)

for i in res:
    print(i)