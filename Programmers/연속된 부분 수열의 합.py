def solution(sequence, k):
    answer = []
    n = len(sequence)
    max_sum = 0
    end = 0
    for index in range(n):
        while max_sum < k and end < n:
            max_sum += sequence[end]
            end += 1

        if max_sum == k:
            answer.append((index, end - 1, end - 1 - index))

        max_sum -= sequence[index]

    answer.sort(key=lambda x: x[2])

    return answer[0][0:2]