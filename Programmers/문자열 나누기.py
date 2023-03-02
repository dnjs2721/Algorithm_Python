def solution(s):
    answer  = 0
    arr = []
    for i in range(len(s)):
        if len(arr) == 0:
            arr.append(s[i])
            answer += 1
            continue
        if s[i] == arr[0]:
            arr.append(s[i])
        else:
            arr.pop()
                              
    return answer

print(solution("banana"	))
print(solution("abracadabra"	))
print(solution("aaabbaccccabba"	))