from collections import deque

def solution(cards1, cards2, goal):
    card1_q = deque(list(cards1))
    card2_q = deque(list(cards2))
    
    for target in goal:
        if card1_q and card1_q[0] == target:
            card1_q.popleft()
        elif card2_q and card2_q[0] == target:
            card2_q.popleft()
        else:
            return "No"
        
    return "Yes"
    
print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"],["want", "to"],["i", "want", "to", "drink", "water"]))