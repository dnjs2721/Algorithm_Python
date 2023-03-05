def solution(food):
    answer = ''
    for i in range(1, len(food)):
        if food[i] > 1:
            for _ in range(int(food[i])//2):
                answer += str(i)
    
    answer += '0'
    
    for i in range(len(answer)-2, -1, -1):
        answer += answer[i]
    
    return answer
    
print(solution([1, 3, 4, 6]	))
print(solution([1, 7, 1, 2]))