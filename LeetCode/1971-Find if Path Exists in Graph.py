from collections import deque
from collections import defaultdict

class Solution:
    def validPath(self, n, edges, source, destination):
        
        if source == destination:
            return True
        
        # visted = [False for _ in range(n)]
        
        dic = defaultdict(list)
        for edge, nextEdge in edges:
            dic[edge].append(nextEdge)
            dic[nextEdge].append(edge)
        
        q = deque()
        q.append(source)
        visted = set([source])
        # visted[source] = True.
        
        while q:
            edge = q.popleft()
            if edge == destination:
                return True
            for nextEdge in dic[edge]:
                # if visted[nextEdge] == False:
                #     visted[nextEdge] = True
                if nextEdge not in visted:
                    visted.add(nextEdge)
                    q.append(nextEdge)
                       
        return False

print(Solution().validPath(3, [[0,1],[1,2],[2,0]], 0, 2))
print(Solution().validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))