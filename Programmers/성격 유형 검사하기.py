from collections import defaultdict

def solution(survey, choices):
    answer = ''
    dic = defaultdict(int)

    for i in range(len(survey)):
        a, b = survey[i]
        point = choices[i]
        if point == 4:
            continue
        elif point <= 3:
            dic[a] = dic[a] + (4-point)
        elif point >= 5:
            dic[b] = dic[b] + (point-4)

    def compare(c, d):
        if dic[c] >= dic[d]:
            return c
        else:
            return d

    for o, t in [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]:
        answer += compare(o, t)

    return answer


print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))