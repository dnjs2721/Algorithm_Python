def solution(name, yearning, photo):
    answer = []
    dic = dict(zip(name, yearning))
    for items in photo:
        temp = 0
        for item in items:
            if item not in dic:
                continue
            temp += dic[item]
        answer.append(temp)
    return answer