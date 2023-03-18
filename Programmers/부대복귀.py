from collections import deque

def solution(n, roads, sources, destination):
    road = [[] for _ in range(n + 1)]
    visited = [-1 for _ in range(n + 1)]
    for s, e in roads:
        road[s].append(e)
        road[e].append(s)
    visited = bfs(destination, road, visited)
    answer = [visited[i] for i in sources]

    return answer

def bfs(dest, graph, vis):
    q = deque([dest])
    vis[dest] = 0
    while q:
        start = q.popleft()
        for end in graph[start]:
            if vis[end] == -1:
                vis[end] = vis[start] + 1
                q.append(end)

    return vis


print(solution(3, [[1, 2], [2, 3]], [2, 3], 1))
print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))
