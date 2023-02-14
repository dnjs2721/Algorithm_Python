import heapq as hq

def scan(dist, graph):
    heap = []
    hq.heappush(heap, [0, 1])
    while heap:
        cost, node = hq.heappop(heap)
        for c, n in graph[node]:
            if cost + c < dist[n]:
                dist[n] = cost + c
                hq.heappush(heap, [cost + c, n])
    
def solution(N, road, K):
    dist = [float('inf')] * (N + 1)
    dist[1] = 0
    graph = [[] for _ in range(N + 1)]
    for start, end, cost in road:
        graph[start].append([cost, end])
        graph[end].append([cost, start])
    scan(dist, graph)
    return len([i for i in dist if i <= K])

print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))