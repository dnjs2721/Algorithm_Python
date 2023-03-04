def solution(number, limit, power):
    answer = 0
    divisor = [1 for _ in range(number + 1)]
    for i in range(2, number + 1):
        for j in range(i, number + 1, i):
            divisor[j] += 1
    
    for i in range(1, number + 1):
        if divisor[i] > limit:
            answer += power
        else:
            answer += divisor[i]
        
    return answer

print(solution(5, 3, 2))
print(solution(10, 3, 2))
