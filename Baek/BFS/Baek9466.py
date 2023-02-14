import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)

def dfs(x):
    global res
    visited[x] = True
    cycle.append(x)
    num = numbers[x]
    if visited[num]:
        if num in cycle:
            res += cycle[cycle.index(num):]
        return
    else:
        dfs(num)


t = int(input())

for _ in range(t):
    n = int(input())
    numbers = [0] + list(map(int, input().rstrip().split()))
    visited = [False] * (n+1)
    res = []

    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)
    
    print(n - len(res))