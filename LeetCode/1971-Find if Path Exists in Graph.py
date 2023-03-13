from collections import deque
from collections import defaultdict

class Solution:
    def validPath(self, n, edges, source, destination):
        
        if source == destination:
            return True
        
        visted = [False for _ in range(n)]
        
        dic = defaultdict(list)
        for edge, nextEdge in edges:
            dic[edge].append(nextEdge)
            dic[nextEdge].append(edge)
        
        q = deque()
        q.append(source)
        visted[source] = True
        
        while q:
            edge = q.popleft()
            for nextEdge in dic[edge]:
                if nextEdge == destination:
                    return True
                if visted[nextEdge] == False:
                    visted[nextEdge] = True
                    q.append(nextEdge)
                       
        return False
        
n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2

print(Solution().validPath(n, edges, source, destination))