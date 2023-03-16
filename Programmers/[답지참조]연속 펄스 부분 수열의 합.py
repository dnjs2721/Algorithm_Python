def solution(sequence):
    answer = 0
    n = len(sequence)

    dp1 = [sequence[i] * (-1) ** i for i in range(n)] # 처음이 1 인 연속 펄스 dp
    dp2 = [sequence[i] * (-1) ** (i + 1) for i in range(n)] # 처음이 -1인 연속 펄스 dp
    seq1 = [sequence[i] * (-1) ** i for i in range(n)] # 처음이 1 인 연속 펄스
    seq2 = [sequence[i] * (-1) ** (i + 1) for i in range(n)] # 처음이 -1인 연속 펄스

    for i in range(n):
        if i >= 1:
            dp1[i] = max(dp1[i - 1] + seq1[i], seq1[i]) # dp1에 대한 부분합 공식
            dp2[i] = max(dp2[i - 1] + seq2[i], seq2[i]) # dp2에 대한 부분합 공식

    return max(max(dp1), max(dp2))


print(solution([2, 3, -6, 1, 3, -1, 2, 4]	))