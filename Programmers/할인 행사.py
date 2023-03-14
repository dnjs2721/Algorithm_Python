from collections import Counter

def solution(want, number, discount):
    answer = 0
    for day in range(0, len(discount)-9):
        discount_count = Counter(discount[day:day+10])
        
        flag = True
        for i in range(len(want)):
            if want[i] not in discount_count:
                flag = False
                break
            if discount_count[want[i]] < number[i]:
                flag = False
                break
        if flag:
            answer += 1
        
    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution(["apple"],[10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))