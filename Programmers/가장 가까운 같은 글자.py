from collections import defaultdict

def solution(s):
    answer = []
    dic = defaultdict(int)
    for i in range(len(s)):
        if dic[s[i]] == 0:
            answer.append(-1)
        else:
            answer.append(i-dic[s[i]]+1)
        dic[s[i]] = i + 1
    return answer

print(solution("banana"	))
print(solution("foobar"))