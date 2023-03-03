from collections import defaultdict

def solution(k, tangerine):
    answer = 0
    dic = defaultdict(int)
    res = 0
    for i in tangerine:
        dic[i] += 1
        
    count = sorted(list(dic.values()), reverse=1)
    
    for i in count:
        answer += 1
        res += i
        if res >= k:
            return answer

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]	))
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]	))
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]	))