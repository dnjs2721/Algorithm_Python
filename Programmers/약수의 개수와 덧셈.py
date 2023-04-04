def solution(left, right):
    answer = 0
    for number in range(left, right + 1):
        temp = 0
        for i in range(1, int(number ** (1 / 2)) + 1):
            if number % i == 0:
                temp += 1
                if i < number // i:
                    temp += 1

        if temp % 2 == 0:
            answer += number
        else:
            answer -= number

    return answer