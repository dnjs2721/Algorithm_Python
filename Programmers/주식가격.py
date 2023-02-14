from collections import deque

def solution(prices):
    answer = []
    q = deque(prices)
    
    while q:
        price = q.popleft()
        sec = 0
        for next_price in q:
            sec += 1
            if price > next_price:
                break
            
        answer.append(sec) 
            
    return answer

print(solution([1, 2, 3, 2, 3]))