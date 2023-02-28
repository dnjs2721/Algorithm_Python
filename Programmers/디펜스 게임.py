import heapq

def solution(n, k, enemy):
    answer = 0
    sumEnemy = 0
    heap = []
    
    if k >= len(enemy) or n >= sum(enemy):
        return len(enemy)
    
    for value in enemy:
        heapq.heappush(heap, -value)
        sumEnemy += value
        if sumEnemy > n:
            if k == 0:
                break
            sumEnemy += heapq.heappop(heap)
            k -= 1
        answer += 1

    return answer

print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]	))
print(solution(2, 4, [3, 3, 3, 3]	))