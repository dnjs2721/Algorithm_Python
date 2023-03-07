def solution(ingredient):
    answer = 0
    idx_check = 0
    
    while idx_check <= len(ingredient)-2:
        if ingredient[idx_check:idx_check+4] == [1,2,3,1]:
            del (ingredient[idx_check:idx_check+4])
            idx_check -= 3
            answer += 1
        idx_check += 1
    
    return answer

print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]	))
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]	))

# 1 2 3 1 일 때 하나