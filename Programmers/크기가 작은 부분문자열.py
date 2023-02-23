def solution(t, p):
    arr = []
    for i in range(len(t)-(len(p)-1)):
        if int(t[i:i+len(p)]) <= int(p):
            arr.append(t[i:i+len(p)])
    return len(arr)

print(solution("3141592", "271"))
print(solution("500220839878", "7"))
print(solution("10203", "15"))