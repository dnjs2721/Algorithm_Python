def solution(topping):
    answer = 0
    count_topping = {}
    for item in topping: # count_topping = Counter(topping)
        if item in count_topping:
            count_topping[item] += 1
        else:
            count_topping[item] = 1
    
    piece = set()
    for item in topping:
        piece.add(item)
        count_topping[item] -= 1
        if count_topping[item] == 0:
            count_topping.pop(item)
        if len(piece) == len(count_topping):
            answer += 1
        if len(piece) > len(count_topping):
            return answer
    return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2]	))
print(solution([1, 2, 3, 1, 4]	))

# 매개변수는 롤케이크 위에 올려진 토핑
# 잘린 조각들의 크기와 올려진 토핑의 개수는 상관 없고
# 각 조각에 동일한 가짓수의 토핑이 올라가면 공평하게 나누어진 것으로 생각
# 토핑의 순서는 변경이 불가능
# 잘린 조각들이 같은 토핑일 필요는 없음 가짓수가 중요
# 공평하게 나눌 수 있는 방법을 return