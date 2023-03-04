import heapq

def solution(k, m, score):
    answer = 0
    heap = []
    for i in score:
        heapq.heappush(heap, -i)
        
    repeat_count = len(heap)//m
    
    for _ in range(repeat_count):
        min_score = k
        for _ in range(m):
            min_score = min(min_score, -heapq.heappop(heap))
        answer += min_score * m
        
    return answer

print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))