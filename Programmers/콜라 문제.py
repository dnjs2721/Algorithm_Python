def solution(a, b, n):
    answer = 0
    while 1:
        if n // a > 0:
            answer += (b * (n // a))
            n = (n % a) + (b * (n // a))
        else:
            break
    return answer

print(solution(2, 1, 20))
print(solution(3, 1, 20))