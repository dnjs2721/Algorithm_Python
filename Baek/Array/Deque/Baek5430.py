import sys
from collections import deque

T =  int(sys.stdin.readline())

for i in range(T):
    f = list(sys.stdin.readline().rstrip())
    arrsize = int(sys.stdin.readline())
    input_arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    rev = 0

    if arrsize > 0:
        arr = deque(input_arr)
    else:
        arr = []

    flag = 1

    for j in f:
        if j == 'R':
            rev += 1
        elif j == 'D':
            if len(arr)==0:
                flag = 0
                print("error")
                break
            else:
                if rev % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()

    if flag:
        if rev %2 == 0:
            print("[" + ','.join(arr) + "]")
        else:
            arr.reverse()
            print("[" + ','.join(arr) + "]")