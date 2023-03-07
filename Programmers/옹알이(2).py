def solution(babbling):
    answer = 0
    possible = ["aya", "ye", "woo", "ma"]
    
    for i in babbling:
        for p in possible:
            if p * 2 not in i:
                i=i.replace(p,' ')
            else:
                break
        if i.strip() == '':
            answer += 1

    return answer

# print(solution(["aya", "yee", "u", "maa"]	))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]	))

# aya, ye, woo, ma