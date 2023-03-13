from collections import Counter

def solution(X, Y):
    answer = ''
    x_dic = Counter(list(X))
    y_dic = Counter(list(Y))
    for num in range(9, -1, -1):
        answer += (str(num) * min(x_dic[str(num)], y_dic[str(num)]))
    
    if len(answer) == 0:
        return '-1'
    if len(answer) == Counter(answer)['0']:
        return '0'
    
    return answer
    
    
    # x_dic = Counter(list(X))
    # y_dic = Counter(list(Y))
    # intersection = list(set(X) & set(Y))
    # intersection.sort(reverse=1)
    
    # if len(intersection) == 0:
    #     return '-1'
    # if len(intersection) == 1 and intersection[0] == '0':
    #     return '0'
    # else:
    #     for item in intersection:
    #         answer += item * min(x_dic[item], y_dic[item])
        
    # return answer
    
print(solution("100", "2345"))
print(solution("100", "203045"))
print(solution("100", "123450"))
print(solution("12321", "42531"))
print(solution("5525", "1255"))

# 1. x 와 y에서 공통적인 수를 찾는다. 공통적인 수의 개수도 구한다 min
# 위 수를 조합하여 가장 큰 수를 만든다.
# 공통적인 수가 0 밖에 없다면 0
# 공통적인 수가 없다면 -1