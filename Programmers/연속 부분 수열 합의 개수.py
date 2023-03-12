def solution(elements):
    answer = set()
    elementLen = len(elements)
    elements = elements * 2

    for i in range(elementLen):
        for j in range(elementLen):
            answer.add(sum(elements[j:j+i+1]))
    return len(answer)

print(solution([7,9,1,1,4]))