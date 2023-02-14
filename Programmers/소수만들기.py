# 소수 만들기
from itertools import combinations

def solution(nums):
    answer = 0
    for i in combinations(nums, 3):
        sum_num = sum(i)
        for j in range(2, sum_num):
            if sum_num % j == 0:
                break
        else:
            answer += 1

    return answer

print(solution([1,2,7,6,4]))