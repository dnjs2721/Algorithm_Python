import heapq

def solution(k, score):
    answer = []
    heap = []
    
    for i in score:
        if len(heap) < k:
            heapq.heappush(heap, i)
        elif len(heap) == k:
            heapq.heappush(heap, i)
            heapq.heappop(heap)
        answer.append(heap[0])
    return answer

print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
print(solution(4,[0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]	 ))