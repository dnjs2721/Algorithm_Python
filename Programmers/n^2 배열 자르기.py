def solution(n, left, right):
    answer = []
    for idx in range(left, right + 1):
        y, x = idx//n, idx % n
        if y >= x:
            answer.append(y + 1)
        elif y < x:
            answer.append(x + 1)

    return answer


print(solution(3, 2, 5))
print(solution(4, 7, 14))
