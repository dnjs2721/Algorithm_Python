def solution(cards):
    answer = 0
    
    visted = [0 for _ in range(len(cards))]
    groupVistedCountlist = []
    
    for idx, nowCard in enumerate(cards):
        if visted[idx] == 0:
            visted[idx] = 1
            groupCount = 1
            next_idx = nowCard-1
            
            while True:
                if visted[next_idx] == 0:
                    groupCount += 1
                    visted[next_idx] = 1
                    next_idx = cards[next_idx] - 1
                else:
                    break
        
            groupVistedCountlist.append(groupCount)
        
    groupVistedCountlist.sort(reverse=1)
        
    if len(groupVistedCountlist) > 1:
        answer = groupVistedCountlist[0] * groupVistedCountlist[1]
    else:
        answer = 0
    
    return answer

print(solution([8,6,3,7,2,5,1,4]))

# 8, 4, 7, 1
# 6, 5, 2