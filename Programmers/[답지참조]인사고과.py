from collections import deque

def solution(scores):
    answer = 0
    target = scores[0]
    target_score = sum(scores[0])
    scores.sort(key=lambda x: (-x[0], x[1]))
    
    print(scores)
        
    
    return answer

print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]]))