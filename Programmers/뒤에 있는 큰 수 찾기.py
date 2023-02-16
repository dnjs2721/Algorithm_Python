from collections import deque

def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    q = deque()
    for i in range(len(numbers)):
        while q:
            if numbers[i] > q[0][0]:
                tmp = q.popleft()
                answer[tmp[1]] = numbers[i]
            else:
                q.appendleft((numbers[i], i))
                break
        if not q:  
            q.appendleft((numbers[i], i))
            
    return answer

# def solution(numbers):
#     stack = []
#     result = [-1] * len(numbers)
#     for i in range(len(numbers)):
#         while stack and numbers[stack[-1]] < numbers[i]:
#             result[stack.pop()] = numbers[i]

#         stack.append(i)

#     return result

print(solution([2, 3, 3, 5]))
print(solution([9, 1, 5, 3, 6, 2]))